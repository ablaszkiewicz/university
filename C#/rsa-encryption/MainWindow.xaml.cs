﻿using System;
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
            AsymetricEncryptButton.IsEnabled = false;
            AsymetricDecryptButton.IsEnabled = false;
        }

        private void RefreshAvailableKeys()
        {
            KeysListBox.Items.Clear();
            foreach (var keyFileName in KeyStorage.GetKeysInDirectory())
            {
                var item = new ListBoxItem();
                var displayedName = "";
                var pureName= keyFileName.Split('.')[0].Split('_')[0];
                var fileSufix= keyFileName.Split('.')[0].Split('_')[1];

                displayedName += pureName;

                if (fileSufix == "PRIVATE")
                {
                    displayedName = "🔒 " + displayedName;
                }
                else displayedName = "     " + displayedName;
                
                item.Selected += KeyStorage.Instance().ChooseKey;
                item.Selected += ChangeButtonsState;
                item.Content = displayedName;
                item.Tag = keyFileName;
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
            RSACrypter.Instance().Encrypt();
        }

        private void AsymetricDecrypt_OnClick(object sender, RoutedEventArgs e)
        {
            RSACrypter.Instance().Decrypt();
        }

        private void AsymetricDropPanel_OnDrop(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                string[] files = (string[]) e.Data.GetData(DataFormats.FileDrop);
                RSACrypter.Instance().SetFileBeingEcryptedPath(files[0]);
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

        private void ChangeButtonsState(object sender, RoutedEventArgs e)
        {
            var item = (ListBoxItem) sender;

            try
            {
                var identifier = item.Tag.ToString().Split('.')[0].Split('_')[1];
                if (identifier == "PRIVATE")
                {
                    AsymetricEncryptButton.IsEnabled = false;
                    AsymetricDecryptButton.IsEnabled = true;
                }
                else if (identifier == "PUBLIC")
                {
                    AsymetricEncryptButton.IsEnabled = true;
                    AsymetricDecryptButton.IsEnabled = false;
                }
                else
                {
                    AsymetricEncryptButton.IsEnabled = false;
                    AsymetricDecryptButton.IsEnabled = false;
                }
            }
            catch (Exception error)
            {
                AsymetricEncryptButton.IsEnabled = false;
                AsymetricDecryptButton.IsEnabled = false;
            }

            
        }
    }
}