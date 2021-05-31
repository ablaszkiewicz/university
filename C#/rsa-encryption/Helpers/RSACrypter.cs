using System;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Windows;

namespace rsa_encryption
{
    public class RSACrypter
    {
        private static RSACrypter _instance;
        public static RSACrypter Instance()
        {
            if (_instance == null)
            {
                _instance = new RSACrypter();
            }
            return _instance;
        }
        
        private String filePath;
        
        public void Encrypt()
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Encrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                try
                {
                    rsa.FromXmlString(File.ReadAllText(keyPath));
                    byte[] bytesToEncrypt = File.ReadAllBytes(filePath);
                    byte[] encrypted = rsa.Encrypt(bytesToEncrypt, false);

                    var pureFileName = Path.GetFileName(filePath).Split('.')[0];
                    var extension = Path.GetFileName(filePath).Split('.')[1];
                    File.WriteAllBytes($"{pureFileName}_ENCRYPTED.{extension}", encrypted);
                    
                    Process.Start("explorer.exe", Directory.GetCurrentDirectory());
                }
                catch (Exception exception)
                {
                    MessageBox.Show("Nieprawidłowy klucz!");
                }
            }
        }
        
        public void Decrypt()
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Decrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(File.ReadAllText(keyPath));
                byte[] bytesToDecrypt = File.ReadAllBytes(filePath);
                try
                {
                    byte[] decrypted = rsa.Decrypt(bytesToDecrypt, false);
                    var decryptedString = Encoding.UTF8.GetString(decrypted);
                    var pureFileName = Path.GetFileName(filePath).Split('.')[0].Split('_')[0];
                    var extension = Path.GetFileName(filePath).Split('.')[1];
                    File.WriteAllText($"{pureFileName}_DECRYPTED.{extension}", decryptedString);
                    Process.Start("explorer.exe", Directory.GetCurrentDirectory());
                }
                catch (Exception exception)
                {
                    MessageBox.Show("Nieprawidłowy klucz!");
                }
            }
        }
        
        public void Encrypt(string path)
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Encrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                try
                {
                    rsa.FromXmlString(File.ReadAllText(keyPath));
                    byte[] bytesToEncrypt = File.ReadAllBytes(path);
                    byte[] encrypted = rsa.Encrypt(bytesToEncrypt, false);

                    var pureFileName = Path.GetFileName(path).Split('.')[0];
                    File.WriteAllBytes($"{pureFileName}_ENCRYPTED.txt", encrypted);
                    
                    Process.Start("explorer.exe", Directory.GetCurrentDirectory());
                }
                catch (Exception exception)
                {
                    MessageBox.Show("Nieprawidłowy klucz!");
                }
            }
        }

        public void Decrypt(string path)
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Decrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(File.ReadAllText(keyPath));
                byte[] bytesToDecrypt = File.ReadAllBytes(path);
                try
                {
                    byte[] decrypted = rsa.Decrypt(bytesToDecrypt, false);
                    var decryptedString = Encoding.UTF8.GetString(decrypted);
                    var pureFileName = Path.GetFileName(path).Split('.')[0].Split('_')[0];
                    File.WriteAllText($"{pureFileName}_DECRYPTED.txt", decryptedString);
                    Process.Start("explorer.exe", Directory.GetCurrentDirectory());
                }
                catch (Exception exception)
                {
                    MessageBox.Show("Nieprawidłowy klucz!");
                }
            }
        }
        
        public void SetFileBeingEcryptedPath(string filePath)
        {
            this.filePath = filePath;
            Console.WriteLine($"Updated RSACrypto file path to: {filePath}");
        }
    }
}