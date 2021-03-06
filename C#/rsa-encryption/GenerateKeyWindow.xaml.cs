using System;
using System.IO;
using System.Security.Cryptography;
using System.Windows;
using System.Windows.Controls;

namespace rsa_encryption
{
    public partial class GenerateKeyWindow : Window
    {
        private Action refreshAvailableKeys;
        public GenerateKeyWindow(Action refreshAvailableKeys)
        {
            InitializeComponent();
            InitializeComboBox();
            this.refreshAvailableKeys = refreshAvailableKeys;
        }

        private void InitializeComboBox()
        {
            foreach (var type in Enum.GetValues(typeof(KeySize)))
            {
                Console.WriteLine(type);
                var item = new ComboBoxItem();
                item.Content = type;
                item.Tag = (int) type;
                AvailableSizeOptions.Items.Add(item);
            }

            AvailableSizeOptions.SelectedIndex = 0;
        }
        
        private void GenerateKeysButton_OnClick(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("Generating asymetric keys...");
            var selected = (ComboBoxItem)AvailableSizeOptions.SelectedItem;
            var rsa = new RSACryptoServiceProvider((int)selected.Tag);
            var publicKey = rsa.ToXmlString(false);
            var privateKey = rsa.ToXmlString(true);

            var fileName = $"{KeyName.Text}_PRIVATE";
            KeyStorage.SaveKeyToFile(fileName, privateKey);
            
            fileName = $"{KeyName.Text}_PUBLIC";
            KeyStorage.SaveKeyToFile(fileName, publicKey);

            refreshAvailableKeys.Invoke();
            Close();
        }
        
        private void GenerateSymetricKeyButton_OnClick(object sender, RoutedEventArgs e)
        {
            Console.WriteLine("Generating symetric key...");
            var aes = new AesCryptoServiceProvider();
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.ANSIX923;
            aes.BlockSize = 128;
            aes.KeySize = 256;
            aes.GenerateKey();
            aes.GenerateIV();

            string[] lines =
            {
                Convert.ToBase64String(aes.IV),
                Convert.ToBase64String(aes.Key),
            };
            
            File.WriteAllLines(SymetricKeyName.Text + ".txt", lines);
            
            Close();
        }
    }
}