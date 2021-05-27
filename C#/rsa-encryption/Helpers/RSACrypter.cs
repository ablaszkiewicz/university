using System;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;
using System.Text;

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
        
        public static void Encrypt()
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Encrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(File.ReadAllText(keyPath));
                //byte[] bytesToEncrypt = Encoding.UTF8.GetBytes(File.ReadAllText("to_encrypt.txt"));
                byte[] bytesToEncrypt = File.ReadAllBytes("to_encrypt.txt");
                byte[] encrypted = rsa.Encrypt(bytesToEncrypt, false);
                File.WriteAllBytes("encrypted.txt", encrypted);
            }
            
            Process.Start("explorer.exe", Directory.GetCurrentDirectory());
        }
        
        public static void Decrypt()
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Decrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(File.ReadAllText(keyPath));
                byte[] bytesToDecrypt = File.ReadAllBytes("encrypted.txt");
                byte[] decrypted = rsa.Decrypt(bytesToDecrypt, false);
                //var decryptedString = BitConverter.ToString(decrypted).Replace("-", "");
                var decryptedString = Encoding.UTF8.GetString(decrypted);
                
                File.WriteAllText("decrypted.txt", decryptedString);
            }
            
            Process.Start("explorer.exe", Directory.GetCurrentDirectory());
        }

        public void SetFilePath(string filePath)
        {
            this.filePath = filePath;
            Console.WriteLine($"Updated RSACrypto file path to: {filePath}");
        }
    }
}