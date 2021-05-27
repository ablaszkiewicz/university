using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Path = System.IO.Path;

namespace rsa_encryption
{
    public partial class MainWindow : Window
    {

        public MainWindow()
        {
            InitializeComponent();
            RefreshAvailableKeys();
        }

        private void RefreshAvailableKeys()
        {
            KeysListBox.Items.Clear();
            foreach (var key in KeyStorage.GetKeysInDirectory())
            {
                var item = new ListBoxItem();
                item.Selected += KeyStorage.Instance().ChooseKey;
                item.Content = key;
                KeysListBox.Items.Add(item);
            }
        }
        
        private void GenerateKeysButton_OnClick(object sender, RoutedEventArgs e)
        {
            GenerateKeyWindow window = new GenerateKeyWindow(RefreshAvailableKeys);
            window.ShowDialog();
        }

        private void AsymetricEncrypt_OnClick(object sender, RoutedEventArgs e)
        {
            RSACrypter.Encrypt();
        }

        private void AsymetricDecrypt_OnClick(object sender, RoutedEventArgs e)
        {
            RSACrypter.Decrypt();
        }

        private void AsymetricDropPanel_OnDrop(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                string[] files = (string[]) e.Data.GetData(DataFormats.FileDrop);
                RSACrypter.Instance().SetFilePath(files[0]);
            }
        }
        
        private void SymetricEncrypt_OnClick(object sender, RoutedEventArgs e)
        {
            throw new NotImplementedException();
        }

        private void SymetricDecrypt_OnClick(object sender, RoutedEventArgs e)
        {
            throw new NotImplementedException();
        }
    }
}