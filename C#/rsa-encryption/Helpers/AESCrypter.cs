using System;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;
using System.Text;
using System.Windows;

namespace rsa_encryption
{
    public class AESCrypter
    {
        private static AESCrypter _instance;
        public static AESCrypter Instance()
        {
            if (_instance == null)
            {
                _instance = new AESCrypter();
            }
            return _instance;
        }
        
        private String filePath;
        private String keyPath;
        
        public void Encrypt()
        {
            AesCryptoServiceProvider cryptoServiceProvider = new AesCryptoServiceProvider();
            cryptoServiceProvider.Mode = CipherMode.CBC;
            cryptoServiceProvider.Padding = PaddingMode.ANSIX923;
            cryptoServiceProvider.BlockSize = 128;
            cryptoServiceProvider.KeySize = 256;
            
            string[] lines = File.ReadAllLines("aes-key.txt");
            byte[] iv = Convert.FromBase64String(lines[0]);
            byte[] key = Convert.FromBase64String(lines[1]);
            cryptoServiceProvider.IV = iv;
            cryptoServiceProvider.Key = key;

            string textToEncrypt = File.ReadAllText(filePath);
            string pureName = Path.GetFileName(filePath).Split(".")[0];
            Console.WriteLine(pureName);
            
            ICryptoTransform transform = cryptoServiceProvider.CreateEncryptor();
            byte[] encryptedBytes =
                transform.TransformFinalBlock(Encoding.UTF8.GetBytes(textToEncrypt), 0, textToEncrypt.Length);

            string encryptedText = Convert.ToBase64String(encryptedBytes);
            File.WriteAllText($"{pureName}_AES-ENCRYPTED.txt", encryptedText);

            RSACrypter.Instance().Encrypt("aes-key.txt");
        }

        public void Decrypt()
        {
            AesCryptoServiceProvider cryptoServiceProvider = new AesCryptoServiceProvider();
            cryptoServiceProvider.Mode = CipherMode.CBC;
            cryptoServiceProvider.Padding = PaddingMode.ANSIX923;
            cryptoServiceProvider.BlockSize = 128;
            cryptoServiceProvider.KeySize = 256;

            RSACrypter.Instance().Decrypt("aes-key_ENCRYPTED.txt");
            string[] lines = File.ReadAllLines("aes-key_DECRYPTED.txt");
            byte[] iv = Convert.FromBase64String(lines[0]);
            byte[] key = Convert.FromBase64String(lines[1]);
            cryptoServiceProvider.IV = iv;
            cryptoServiceProvider.Key = key;

            ICryptoTransform transform = cryptoServiceProvider.CreateEncryptor();
            transform = cryptoServiceProvider.CreateDecryptor();
            
            byte[] encryptedBytes = Convert.FromBase64String(File.ReadAllText(filePath));
            byte[] decryptedBytes = transform.TransformFinalBlock(encryptedBytes, 0, encryptedBytes.Length);
            string decryptedText = Encoding.UTF8.GetString(decryptedBytes);
            
            Console.WriteLine(decryptedText);
            string pureName = Path.GetFileName(filePath).Split("_")[0];
            File.WriteAllText($"{pureName}_AES_DECRYPTED.txt", decryptedText);
        }
        
        public void SetFileBeingEcryptedPath(string filePath)
        {
            this.filePath = filePath;
            Console.WriteLine($"Updated AESCrypto file path to: {filePath}");
        }
        
        public void SetKeyFilePath(string keyPath)
        {
            this.keyPath = keyPath;
            Console.WriteLine($"Updated AESCrypto key path to: {filePath}");
        }
    }
}