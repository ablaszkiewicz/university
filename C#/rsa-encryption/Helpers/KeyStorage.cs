using System;
using System.Collections.Generic;
using System.IO;
using System.Security.Cryptography;
using System.Windows;
using System.Windows.Controls;

namespace rsa_encryption
{
    public class KeyStorage
    {
        private static KeyStorage _instance;
        public static KeyStorage Instance()
        {
            if (_instance == null)
            {
                _instance = new KeyStorage();
            }
            return _instance;
        }

        private string keyFile;
        
        public static List<String> GetKeysInDirectory()
        {
            List<String> keys = new List<string>();
            var directoryInfo = new DirectoryInfo(Directory.GetCurrentDirectory());
            foreach (FileInfo file in directoryInfo.GetFiles("*.key"))
            {
                keys.Add(file.Name);
            }

            return keys;
        }
        public static void SaveKeyToFile(string fileName, string text)
        {
            using (StreamWriter writer = new StreamWriter(fileName + ".key"))
            {
                Console.WriteLine($"Saving key to {fileName}.key");
                writer.Write(text);
            }
        }

        public void ChooseKey(object sender, RoutedEventArgs e)
        {
            var item = (ListBoxItem) sender;
            Console.WriteLine($"Chosen new key file: {item.Tag}");
            keyFile = item.Tag.ToString();
        }

        public string GetKeyPath()
        {
            return keyFile;
        }
    }
}