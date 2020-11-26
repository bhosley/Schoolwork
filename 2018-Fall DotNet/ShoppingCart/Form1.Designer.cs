namespace ShoppingCart
{
    partial class Form1
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
            this.InventorySelector = new System.Windows.Forms.ComboBox();
            this.inventoryBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.dotNetShopDataSet = new ShoppingCart.DotNetShopDataSet();
            this.ItemLabel = new System.Windows.Forms.Label();
            this.PriceLabel = new System.Windows.Forms.Label();
            this.PriceDisplay = new System.Windows.Forms.TextBox();
            this.QuantityLabel = new System.Windows.Forms.Label();
            this.SubtotalLabel = new System.Windows.Forms.Label();
            this.QuantitySelector = new System.Windows.Forms.NumericUpDown();
            this.SubtotalDisplay = new System.Windows.Forms.TextBox();
            this.AddToCartButton = new System.Windows.Forms.Button();
            this.RemoveFromCartButton = new System.Windows.Forms.Button();
            this.CartLabel = new System.Windows.Forms.Label();
            this.CheckOutButton = new System.Windows.Forms.Button();
            this.TotalLabel = new System.Windows.Forms.Label();
            this.TotalDisplay = new System.Windows.Forms.TextBox();
            this.inventoryTableAdapter = new ShoppingCart.DotNetShopDataSetTableAdapters.InventoryTableAdapter();
            this.CartDisplay = new System.Windows.Forms.DataGridView();
            this.NewItemButton = new System.Windows.Forms.Button();
            this.EditInventoryButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.inventoryBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dotNetShopDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.QuantitySelector)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.CartDisplay)).BeginInit();
            this.SuspendLayout();
            // 
            // InventorySelector
            // 
            this.InventorySelector.DataSource = this.inventoryBindingSource;
            this.InventorySelector.DisplayMember = "ItemName";
            this.InventorySelector.FormattingEnabled = true;
            this.InventorySelector.Location = new System.Drawing.Point(12, 32);
            this.InventorySelector.Name = "InventorySelector";
            this.InventorySelector.Size = new System.Drawing.Size(172, 21);
            this.InventorySelector.TabIndex = 0;
            this.InventorySelector.ValueMember = "ItemID";
            this.InventorySelector.SelectedValueChanged += new System.EventHandler(this.SelectedItemChanged);
            // 
            // inventoryBindingSource
            // 
            this.inventoryBindingSource.DataMember = "Inventory";
            this.inventoryBindingSource.DataSource = this.dotNetShopDataSet;
            // 
            // dotNetShopDataSet
            // 
            this.dotNetShopDataSet.DataSetName = "DotNetShopDataSet";
            this.dotNetShopDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // ItemLabel
            // 
            this.ItemLabel.AutoSize = true;
            this.ItemLabel.Location = new System.Drawing.Point(12, 10);
            this.ItemLabel.Name = "ItemLabel";
            this.ItemLabel.Size = new System.Drawing.Size(30, 13);
            this.ItemLabel.TabIndex = 1;
            this.ItemLabel.Text = "Item:";
            // 
            // PriceLabel
            // 
            this.PriceLabel.AutoSize = true;
            this.PriceLabel.Location = new System.Drawing.Point(205, 10);
            this.PriceLabel.Name = "PriceLabel";
            this.PriceLabel.Size = new System.Drawing.Size(34, 13);
            this.PriceLabel.TabIndex = 2;
            this.PriceLabel.Text = "Price:";
            // 
            // PriceDisplay
            // 
            this.PriceDisplay.Location = new System.Drawing.Point(208, 32);
            this.PriceDisplay.Name = "PriceDisplay";
            this.PriceDisplay.ReadOnly = true;
            this.PriceDisplay.Size = new System.Drawing.Size(66, 20);
            this.PriceDisplay.TabIndex = 3;
            // 
            // QuantityLabel
            // 
            this.QuantityLabel.AutoSize = true;
            this.QuantityLabel.Location = new System.Drawing.Point(15, 69);
            this.QuantityLabel.Name = "QuantityLabel";
            this.QuantityLabel.Size = new System.Drawing.Size(49, 13);
            this.QuantityLabel.TabIndex = 4;
            this.QuantityLabel.Text = "Quantity:";
            // 
            // SubtotalLabel
            // 
            this.SubtotalLabel.AutoSize = true;
            this.SubtotalLabel.Location = new System.Drawing.Point(205, 69);
            this.SubtotalLabel.Name = "SubtotalLabel";
            this.SubtotalLabel.Size = new System.Drawing.Size(49, 13);
            this.SubtotalLabel.TabIndex = 5;
            this.SubtotalLabel.Text = "Subtotal:";
            // 
            // QuantitySelector
            // 
            this.QuantitySelector.Location = new System.Drawing.Point(16, 97);
            this.QuantitySelector.Maximum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.QuantitySelector.Name = "QuantitySelector";
            this.QuantitySelector.Size = new System.Drawing.Size(86, 20);
            this.QuantitySelector.TabIndex = 6;
            this.QuantitySelector.ValueChanged += new System.EventHandler(this.QuantityChanged);
            // 
            // SubtotalDisplay
            // 
            this.SubtotalDisplay.Location = new System.Drawing.Point(184, 97);
            this.SubtotalDisplay.Name = "SubtotalDisplay";
            this.SubtotalDisplay.ReadOnly = true;
            this.SubtotalDisplay.Size = new System.Drawing.Size(90, 20);
            this.SubtotalDisplay.TabIndex = 7;
            // 
            // AddToCartButton
            // 
            this.AddToCartButton.Location = new System.Drawing.Point(19, 133);
            this.AddToCartButton.Name = "AddToCartButton";
            this.AddToCartButton.Size = new System.Drawing.Size(111, 23);
            this.AddToCartButton.TabIndex = 8;
            this.AddToCartButton.Text = "Add to Cart";
            this.AddToCartButton.UseVisualStyleBackColor = true;
            this.AddToCartButton.Click += new System.EventHandler(this.AddToCartClick);
            // 
            // RemoveFromCartButton
            // 
            this.RemoveFromCartButton.Location = new System.Drawing.Point(163, 133);
            this.RemoveFromCartButton.Name = "RemoveFromCartButton";
            this.RemoveFromCartButton.Size = new System.Drawing.Size(112, 23);
            this.RemoveFromCartButton.TabIndex = 9;
            this.RemoveFromCartButton.Text = "Remove From Cart";
            this.RemoveFromCartButton.UseVisualStyleBackColor = true;
            this.RemoveFromCartButton.Click += new System.EventHandler(this.RemoveFromCartClick);
            // 
            // CartLabel
            // 
            this.CartLabel.AutoSize = true;
            this.CartLabel.Location = new System.Drawing.Point(307, 10);
            this.CartLabel.Name = "CartLabel";
            this.CartLabel.Size = new System.Drawing.Size(29, 13);
            this.CartLabel.TabIndex = 11;
            this.CartLabel.Text = "Cart:";
            // 
            // CheckOutButton
            // 
            this.CheckOutButton.Location = new System.Drawing.Point(21, 173);
            this.CheckOutButton.Name = "CheckOutButton";
            this.CheckOutButton.Size = new System.Drawing.Size(253, 43);
            this.CheckOutButton.TabIndex = 12;
            this.CheckOutButton.Text = "Check Out";
            this.CheckOutButton.UseVisualStyleBackColor = true;
            this.CheckOutButton.Click += new System.EventHandler(this.CheckOutClick);
            // 
            // TotalLabel
            // 
            this.TotalLabel.AutoSize = true;
            this.TotalLabel.Location = new System.Drawing.Point(307, 219);
            this.TotalLabel.Name = "TotalLabel";
            this.TotalLabel.Size = new System.Drawing.Size(34, 13);
            this.TotalLabel.TabIndex = 13;
            this.TotalLabel.Text = "Total:";
            // 
            // TotalDisplay
            // 
            this.TotalDisplay.Location = new System.Drawing.Point(347, 216);
            this.TotalDisplay.Name = "TotalDisplay";
            this.TotalDisplay.ReadOnly = true;
            this.TotalDisplay.Size = new System.Drawing.Size(206, 20);
            this.TotalDisplay.TabIndex = 14;
            this.TotalDisplay.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            // 
            // inventoryTableAdapter
            // 
            this.inventoryTableAdapter.ClearBeforeFill = true;
            // 
            // CartDisplay
            // 
            this.CartDisplay.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.CartDisplay.Location = new System.Drawing.Point(309, 30);
            this.CartDisplay.Name = "CartDisplay";
            this.CartDisplay.Size = new System.Drawing.Size(243, 186);
            this.CartDisplay.TabIndex = 15;
            // 
            // NewItemButton
            // 
            this.NewItemButton.Location = new System.Drawing.Point(18, 232);
            this.NewItemButton.Name = "NewItemButton";
            this.NewItemButton.Size = new System.Drawing.Size(112, 23);
            this.NewItemButton.TabIndex = 16;
            this.NewItemButton.Text = "New Item";
            this.NewItemButton.UseVisualStyleBackColor = true;
            this.NewItemButton.Click += new System.EventHandler(this.NewItemClick);
            // 
            // EditInventoryButton
            // 
            this.EditInventoryButton.Location = new System.Drawing.Point(163, 232);
            this.EditInventoryButton.Name = "EditInventoryButton";
            this.EditInventoryButton.Size = new System.Drawing.Size(111, 23);
            this.EditInventoryButton.TabIndex = 18;
            this.EditInventoryButton.Text = "Edit Inventory";
            this.EditInventoryButton.UseVisualStyleBackColor = true;
            this.EditInventoryButton.Click += new System.EventHandler(this.EditInventoryClick);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(581, 258);
            this.Controls.Add(this.EditInventoryButton);
            this.Controls.Add(this.NewItemButton);
            this.Controls.Add(this.CartDisplay);
            this.Controls.Add(this.TotalDisplay);
            this.Controls.Add(this.TotalLabel);
            this.Controls.Add(this.CheckOutButton);
            this.Controls.Add(this.CartLabel);
            this.Controls.Add(this.RemoveFromCartButton);
            this.Controls.Add(this.AddToCartButton);
            this.Controls.Add(this.SubtotalDisplay);
            this.Controls.Add(this.QuantitySelector);
            this.Controls.Add(this.SubtotalLabel);
            this.Controls.Add(this.QuantityLabel);
            this.Controls.Add(this.PriceDisplay);
            this.Controls.Add(this.PriceLabel);
            this.Controls.Add(this.ItemLabel);
            this.Controls.Add(this.InventorySelector);
            this.Name = "Form1";
            this.Text = "Shopping Cart";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.inventoryBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dotNetShopDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.QuantitySelector)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.CartDisplay)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox InventorySelector;
        private System.Windows.Forms.Label ItemLabel;
        private System.Windows.Forms.Label PriceLabel;
        private System.Windows.Forms.TextBox PriceDisplay;
        private System.Windows.Forms.Label QuantityLabel;
        private System.Windows.Forms.Label SubtotalLabel;
        private System.Windows.Forms.NumericUpDown QuantitySelector;
        private System.Windows.Forms.TextBox SubtotalDisplay;
        private System.Windows.Forms.Button AddToCartButton;
        private System.Windows.Forms.Button RemoveFromCartButton;
        private System.Windows.Forms.Label CartLabel;
        private System.Windows.Forms.Button CheckOutButton;
        private System.Windows.Forms.Label TotalLabel;
        private System.Windows.Forms.TextBox TotalDisplay;
        private DotNetShopDataSet dotNetShopDataSet;
        private System.Windows.Forms.BindingSource inventoryBindingSource;
        private DotNetShopDataSetTableAdapters.InventoryTableAdapter inventoryTableAdapter;
        private System.Windows.Forms.DataGridView CartDisplay;
        private System.Windows.Forms.Button NewItemButton;
        private System.Windows.Forms.Button EditInventoryButton;
    }
}

