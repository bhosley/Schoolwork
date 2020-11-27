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
    public partial class NewItemForm : Form
    {
        StoreItemDataClassesDataContext dc;
        public NewItemForm(StoreItemDataClassesDataContext _dc)
        {
            dc = _dc;
            InitializeComponent();
        }

        private void SubmitClick(object sender, EventArgs e)
        {
            if (EntriesAreValid())
                SubmitItem();
            else
                DisplayError();
        }

        string ErrorMessage = "";
        private bool EntriesAreValid()
        {
            ErrorMessage = "";
            bool Result = true;
            int i;
            decimal d;
            if (false) // Name is valid :Currently no parameters: 
            {
                ErrorMessage += "Name is invald.\n";
                Result = false;
            }
            if (!Decimal.TryParse(PriceEntry.Text, out d ) ) // Price is Valid
            {
                ErrorMessage += "Price is invald.\n";
                Result = false;
            }
            if (!Int32.TryParse(QuantityEntry.Text, out i ) ) // Quantity is Valid
            {
                ErrorMessage += "Quantity is invald.\n";
                Result = false;
            }
            return Result;
        }

        private void SubmitItem()
        {
            Item i = new Item();
            i.ItemID = NewItemID();
            i.ItemName = NameEntry.Text;
            i.UnitPrice = Decimal.Parse(PriceEntry.Text);
            i.Quantity = Int32.Parse(QuantityEntry.Text);
            dc.Items.InsertOnSubmit(i);
            dc.SubmitChanges();
            this.Close();
        }
        private int NewItemID()
        {
            int ContestantID = 1;
            bool IDAccepted = false;
            do
            {
                if (dc.Items.Where(i => i.ItemID == ContestantID).Any())
                    ContestantID++;
                else
                    IDAccepted = true;
            }
            while (!IDAccepted);
            return ContestantID;
        }

        private void DisplayError()
        {
            MessageBox.Show(ErrorMessage, "Entry Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}
