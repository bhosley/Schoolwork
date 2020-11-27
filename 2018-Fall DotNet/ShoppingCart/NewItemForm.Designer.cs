namespace ShoppingCart
{
    partial class NewItemForm
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
            this.PriceEntry = new System.Windows.Forms.TextBox();
            this.PriceLabel = new System.Windows.Forms.Label();
            this.ItemLabel = new System.Windows.Forms.Label();
            this.NameEntry = new System.Windows.Forms.TextBox();
            this.QuantityEntry = new System.Windows.Forms.TextBox();
            this.QuantityLabel = new System.Windows.Forms.Label();
            this.SubmitButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // PriceEntry
            // 
            this.PriceEntry.Location = new System.Drawing.Point(12, 85);
            this.PriceEntry.Name = "PriceEntry";
            this.PriceEntry.Size = new System.Drawing.Size(74, 20);
            this.PriceEntry.TabIndex = 2;
            // 
            // PriceLabel
            // 
            this.PriceLabel.AutoSize = true;
            this.PriceLabel.Location = new System.Drawing.Point(9, 63);
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
            this.ItemLabel.Size = new System.Drawing.Size(61, 13);
            this.ItemLabel.TabIndex = 5;
            this.ItemLabel.Text = "Item Name:";
            // 
            // NameEntry
            // 
            this.NameEntry.Location = new System.Drawing.Point(12, 31);
            this.NameEntry.Name = "NameEntry";
            this.NameEntry.Size = new System.Drawing.Size(179, 20);
            this.NameEntry.TabIndex = 1;
            // 
            // QuantityEntry
            // 
            this.QuantityEntry.Location = new System.Drawing.Point(113, 85);
            this.QuantityEntry.Name = "QuantityEntry";
            this.QuantityEntry.Size = new System.Drawing.Size(78, 20);
            this.QuantityEntry.TabIndex = 3;
            // 
            // QuantityLabel
            // 
            this.QuantityLabel.AutoSize = true;
            this.QuantityLabel.Location = new System.Drawing.Point(110, 63);
            this.QuantityLabel.Name = "QuantityLabel";
            this.QuantityLabel.Size = new System.Drawing.Size(49, 13);
            this.QuantityLabel.TabIndex = 6;
            this.QuantityLabel.Text = "Quantity:";
            // 
            // SubmitButton
            // 
            this.SubmitButton.Location = new System.Drawing.Point(12, 121);
            this.SubmitButton.Name = "SubmitButton";
            this.SubmitButton.Size = new System.Drawing.Size(179, 23);
            this.SubmitButton.TabIndex = 4;
            this.SubmitButton.Text = "Submit";
            this.SubmitButton.UseVisualStyleBackColor = true;
            this.SubmitButton.Click += new System.EventHandler(this.SubmitClick);
            // 
            // NewItemForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(205, 158);
            this.Controls.Add(this.SubmitButton);
            this.Controls.Add(this.QuantityLabel);
            this.Controls.Add(this.QuantityEntry);
            this.Controls.Add(this.NameEntry);
            this.Controls.Add(this.PriceEntry);
            this.Controls.Add(this.PriceLabel);
            this.Controls.Add(this.ItemLabel);
            this.Name = "NewItemForm";
            this.Text = "NewItemForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox PriceEntry;
        private System.Windows.Forms.Label PriceLabel;
        private System.Windows.Forms.Label ItemLabel;
        private System.Windows.Forms.TextBox NameEntry;
        private System.Windows.Forms.TextBox QuantityEntry;
        private System.Windows.Forms.Label QuantityLabel;
        private System.Windows.Forms.Button SubmitButton;
    }
}