using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ShoppingCart
{
    public partial class Form1 : Form
    {
        StoreItemDataClassesDataContext dc = new StoreItemDataClassesDataContext();
        BindingList<Item> CurrentCart = new BindingList<Item>();
        Item CurrentItem = new Item();
        Decimal CurrentTotal = 0.0M;
        public Form1()
        {
            InitializeComponent();
            CartDisplay.DataSource = CurrentCart;
            CartDisplay.Columns["ItemID"].Visible = false;
            CartDisplay.Columns["Description"].Visible = false;
            CartDisplay.Columns["Picture"].Visible = false;
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'dotNetShopDataSet.Inventory' table. You can move, or remove it, as needed.
            this.inventoryTableAdapter.Fill(this.dotNetShopDataSet.Inventory);

        }

        /*
         *  Event Listeners
         */
        private void SelectedItemChanged(object sender, EventArgs e)
        {
            UpdateCurrentItem();
        }

        private void QuantityChanged(object sender, EventArgs e)
        {
            CurrentItem.Quantity = GetQuantity();
            UpdateSubTotal();
        }

        private void AddToCartClick(object sender, EventArgs e)
        {
            if (CheckCartForDuplicates(CurrentItem))
            {
                Item i = GetItemByName(CurrentItem.ItemName);
                i.Quantity += CurrentItem.Quantity;
            }
            else
            {
                Item i = new Item(CurrentItem);
                CurrentCart.Add(i);
            }
            UpdateTotal();
            QuantitySelector.Value = 0;
            UpdateCurrentItem();
        }

        // Add to Cart Helpers
        private int GetQuantity() => Convert.ToInt32(QuantitySelector.Value);

        private bool CheckCartForDuplicates(Item i)
        {
            bool result = false;
            foreach(Item o in CurrentCart)
            {
                if (o.ItemID == i.ItemID)
                {
                    result = true;
                    break;
                }
            }
            return result;
        }

        private Item GetItemByName(String name)
        {
            foreach (Item o in CurrentCart)
            {
                if (o.ItemName == name)
                    return o;
            }
            return null;
        }
        // End Add to Cart Helpers

        private void RemoveFromCartClick(object sender, EventArgs e)
        {       
            CurrentCart.Remove((Item)CartDisplay.CurrentRow.DataBoundItem);
            UpdateTotal();
        }
        
        private void CheckOutClick(object sender, EventArgs e)
        {
            // decrease shop inventory
            List<Item> PurchasedItems = new List<Item>();
            foreach(Item i in CurrentCart)
                PurchasedItems.Add(dc.Items.Where(item => item.ItemID == i.ItemID).Single());
            foreach (Item i in PurchasedItems)
                i.Quantity -= GetItemByName(i.ItemName).Quantity;
            // Create Transaction
            Transaction CurrentTransaction = new Transaction();
            CurrentTransaction.TransactionID = NewTransactionID();
            CurrentTransaction.NetTotal = CurrentTotal;
            dc.Transactions.InsertOnSubmit(CurrentTransaction);
            // Submit Transaction Contents
            int HolderID = NewTransactionContentID();
            foreach (Item i in CurrentCart)
            {
                TransactionContent tc = new TransactionContent();
                tc.TransactionEntryID = HolderID++;
                tc.TransactionID = CurrentTransaction.TransactionID;
                tc.ItemID = i.ItemID;
                tc.Quantity = i.Quantity;
                tc.Price = i.UnitPrice;
                dc.TransactionContents.InsertOnSubmit(tc);
            }
            // Submit Changes to DB and Clear the cart
            dc.SubmitChanges();
            CurrentCart.Clear();
        }

        // Check Out Helpers
        private int NewTransactionID()
        {
            int ContestantID = 1;
            bool IDAccepted = false;
            do
            {
                if (dc.Transactions.Where(i => i.TransactionID == ContestantID).Any())
                    ContestantID++;
                else
                    IDAccepted = true;
            }
            while (!IDAccepted);
            return ContestantID;
        }
        private int NewTransactionContentID()
        {
            int ContestantID = 1;
            bool IDAccepted = false;
            do
            {
                if (dc.TransactionContents.Where(i => i.TransactionEntryID == ContestantID).Any())
                    ContestantID++;
                else
                    IDAccepted = true;
            }
            while (!IDAccepted);
            return ContestantID;
        }
        // End Check Out Helpers

        private void NewItemClick(object sender, EventArgs e)
        {
            NewItemForm nif = new NewItemForm(dc);
            nif.ShowDialog();
            Form1_Load(null, EventArgs.Empty);
        }
        private void EditInventoryClick(object sender, EventArgs e)
        {
            UpdateInventoryForm uif = new UpdateInventoryForm(dc);
            uif.ShowDialog();
            this.Update();
        }

        // General Helpers
        private void UpdateTotal()
        {
            CurrentTotal = 0.0M;
            foreach(Item i in CurrentCart)
                CurrentTotal += (i.Quantity * (decimal)i.UnitPrice);
            TotalDisplay.Text = $"${CurrentTotal.ToString()}";
        }

        private void UpdateSubTotal() => SubtotalDisplay.Text = $"${(CurrentItem.UnitPrice * CurrentItem.Quantity)}";

        private void UpdateCurrentItem()
        {
            try
            {
                DataRowView srow = (DataRowView)InventorySelector.SelectedItem;
                DataRow row = srow.Row;
                CurrentItem.ItemID = (int)row[0];
                CurrentItem.ItemName = (string)row[1];
                CurrentItem.UnitPrice = (decimal)row[2];
                PriceDisplay.Text = $"${CurrentItem.UnitPrice}";
                QuantitySelector.Maximum = decimal.Parse(row[3].ToString());    //row[3] is Quantity
            }
            catch
            {
                //TODO
            }
            QuantitySelector.Value = 0;
            UpdateSubTotal();
        }
    }
}
