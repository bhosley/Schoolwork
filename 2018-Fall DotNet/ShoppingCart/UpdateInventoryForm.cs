using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ShoppingCart
{
    public partial class UpdateInventoryForm : Form
    {
        StoreItemDataClassesDataContext dc;
        Item CurrentItem = new Item();
        public UpdateInventoryForm(StoreItemDataClassesDataContext _dc)
        {
            dc = _dc;
            InitializeComponent();
        }

        private void SubmitClick(object sender, EventArgs e)
        {
            Item i = dc.Items.Where(item => item.ItemID == CurrentItem.ItemID).Single();
            bool ChangeOccured = false;
            if (i.UnitPrice != CurrentItem.UnitPrice) // Price has Changed
            {
                i.UnitPrice = CurrentItem.UnitPrice;
                ChangeOccured = true;
            }
            if (i.Quantity != CurrentItem.Quantity) // Quantity has Changed
            {
                i.Quantity = CurrentItem.Quantity;
                ChangeOccured = true;
            }
            if (ChangeOccured)
                dc.SubmitChanges();
        }

        private void SelectedItemChanged(object sender, EventArgs e)
        {
            try
            {
                DataRowView srow = (DataRowView)InventorySelector.SelectedItem;
                DataRow row = srow.Row;
                CurrentItem.ItemID = (int)row[0];
                CurrentItem.ItemName = (string)row[1];
                CurrentItem.UnitPrice = (decimal)row[2];
                PriceField.Text = $"${CurrentItem.UnitPrice}";
                QuantityField.Text = row[3].ToString();    //row[3] is Quantity
            }
            catch
            {
                //TODO
            }

        }

        private void UpdateInventoryForm_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'dotNetShopDataSet.Inventory' table. You can move, or remove it, as needed.
            this.inventoryTableAdapter.Fill(this.dotNetShopDataSet.Inventory);

        }
    }
}
