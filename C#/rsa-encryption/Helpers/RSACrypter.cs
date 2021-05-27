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
        
        public void Encrypt()
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Encrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(File.ReadAllText(keyPath));
                byte[] bytesToEncrypt = File.ReadAllBytes(filePath);
                byte[] encrypted = rsa.Encrypt(bytesToEncrypt, false);

                var pureFileName = Path.GetFileName(filePath).Split('.')[0];
                File.WriteAllBytes($"{pureFileName}_ENCRYPTED.txt", encrypted);
            }
            
            Process.Start("explorer.exe", Directory.GetCurrentDirectory());
        }
        
        public void Decrypt()
        {
            string keyPath = KeyStorage.Instance().GetKeyPath();
            Console.WriteLine($"Decrypting the file using {keyPath} key");
            
            using (var rsa = new RSACryptoServiceProvider())
            {
                rsa.FromXmlString(File.ReadAllText(keyPath));
                byte[] bytesToDecrypt = File.ReadAllBytes(filePath);
                byte[] decrypted = rsa.Decrypt(bytesToDecrypt, false);
                var decryptedString = Encoding.UTF8.GetString(decrypted);
                
                var pureFileName = Path.GetFileName(filePath).Split('.')[0].Split('_')[0];
                File.WriteAllText($"{pureFileName}_DECRYPTED.txt", decryptedString);
            }
            
            Process.Start("explorer.exe", Directory.GetCurrentDirectory());
        }

        public void SetFileBeingEcryptedPath(string filePath)
        {
            this.filePath = filePath;
            Console.WriteLine($"Updated RSACrypto file path to: {filePath}");
        }
    }
}