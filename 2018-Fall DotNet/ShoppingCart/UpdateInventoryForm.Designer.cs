namespace ShoppingCart
{
    partial class UpdateInventoryForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.PriceField = new System.Windows.Forms.TextBox();
            this.PriceLabel = new System.Windows.Forms.Label();
            this.ItemLabel = new System.Windows.Forms.Label();
            this.InventorySelector = new System.Windows.Forms.ComboBox();
            this.QuantityField = new System.Windows.Forms.TextBox();
            this.QuantityLabel = new System.Windows.Forms.Label();
            this.SubmitChangesButton = new System.Windows.Forms.Button();
            this.dotNetShopDataSet = new ShoppingCart.DotNetShopDataSet();
            this.inventoryBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.inventoryTableAdapter = new ShoppingCart.DotNetShopDataSetTableAdapters.InventoryTableAdapter();
            ((System.ComponentModel.ISupportInitialize)(this.dotNetShopDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.inventoryBindingSource)).BeginInit();
            this.SuspendLayout();
            // 
            // PriceField
            // 
            this.PriceField.Location = new System.Drawing.Point(12, 81);
            this.PriceField.Name = "PriceField";
            this.PriceField.Size = new System.Drawing.Size(81, 20);
            this.PriceField.TabIndex = 7;
            // 
            // PriceLabel
            // 
            this.PriceLabel.AutoSize = true;
            this.PriceLabel.Location = new System.Drawing.Point(12, 65);
            this.PriceLabel.Name = "PriceLabel";
            this.PriceLabel.Size = new System.Drawing.Size(34, 13);
            this.PriceLabel.TabIndex = 6;
            this.PriceLabel.Text = "Price:";
            // 
            // ItemLabel
            // 
            this.ItemLabel.AutoSize = true;
            this.ItemLabel.Location = new System.Drawing.Point(12, 9);
            this.ItemLabel.Name = "ItemLabel";
            this.ItemLabel.Size = new System.Drawing.Size(30, 13);
            this.ItemLabel.TabIndex = 5;
            this.ItemLabel.Text = "Item:";
            // 
            // InventorySelector
            // 
            this.InventorySelector.DataSource = this.inventoryBindingSource;
            this.InventorySelector.DisplayMember = "ItemName";
            this.InventorySelector.FormattingEnabled = true;
            this.InventorySelector.Location = new System.Drawing.Point(12, 31);
            this.InventorySelector.Name = "InventorySelector";
            this.InventorySelector.Size = new System.Drawing.Size(190, 21);
            this.InventorySelector.TabIndex = 4;
            this.InventorySelector.ValueMember = "ItemID";
            this.InventorySelector.SelectedValueChanged += new System.EventHandler(this.SelectedItemChanged);
            // 
            // QuantityField
            // 
            this.QuantityField.Location = new System.Drawing.Point(119, 81);
            this.QuantityField.Name = "QuantityField";
            this.QuantityField.Size = new System.Drawing.Size(83, 20);
            this.QuantityField.TabIndex = 9;
            // 
            // QuantityLabel
            // 
            this.QuantityLabel.AutoSize = true;
            this.QuantityLabel.Location = new System.Drawing.Point(119, 65);
            this.QuantityLabel.Name = "QuantityLabel";
            this.QuantityLabel.Size = new System.Drawing.Size(49, 13);
            this.QuantityLabel.TabIndex = 8;
            this.QuantityLabel.Text = "Quantity:";
            // 
            // SubmitChangesButton
            // 
            this.SubmitChangesButton.Location = new System.Drawing.Point(12, 117);
            this.SubmitChangesButton.Name = "SubmitChangesButton";
            this.SubmitChangesButton.Size = new System.Drawing.Size(190, 23);
            this.SubmitChangesButton.TabIndex = 10;
            this.SubmitChangesButton.Text = "Submit Changes";
            this.SubmitChangesButton.UseVisualStyleBackColor = true;
            this.SubmitChangesButton.Click += new System.EventHandler(this.SubmitClick);
            // 
            // dotNetShopDataSet
            // 
            this.dotNetShopDataSet.DataSetName = "DotNetShopDataSet";
            this.dotNetShopDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // inventoryBindingSource
            // 
            this.inventoryBindingSource.DataMember = "Inventory";
            this.inventoryBindingSource.DataSource = this.dotNetShopDataSet;
            // 
            // inventoryTableAdapter
            // 
            this.inventoryTableAdapter.ClearBeforeFill = true;
            // 
            // UpdateInventoryForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(214, 157);
            this.Controls.Add(this.SubmitChangesButton);
            this.Controls.Add(this.QuantityField);
            this.Controls.Add(this.QuantityLabel);
            this.Controls.Add(this.PriceField);
            this.Controls.Add(this.PriceLabel);
            this.Controls.Add(this.ItemLabel);
            this.Controls.Add(this.InventorySelector);
            this.Name = "UpdateInventoryForm";
            this.Text = "UpdateInventoryForm";
            this.Load += new System.EventHandler(this.UpdateInventoryForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dotNetShopDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.inventoryBindingSource)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox PriceField;
        private System.Windows.Forms.Label PriceLabel;
        private System.Windows.Forms.Label ItemLabel;
        private System.Windows.Forms.ComboBox InventorySelector;
        private System.Windows.Forms.TextBox QuantityField;
        private System.Windows.Forms.Label QuantityLabel;
        private System.Windows.Forms.Button SubmitChangesButton;
        private DotNetShopDataSet dotNetShopDataSet;
        private System.Windows.Forms.BindingSource inventoryBindingSource;
        private DotNetShopDataSetTableAdapters.InventoryTableAdapter inventoryTableAdapter;
    }
}