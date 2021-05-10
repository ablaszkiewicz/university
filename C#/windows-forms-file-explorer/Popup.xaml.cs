using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Windows;

namespace windows_forms
{
    public partial class Popup : Window
    {
        private string path;
        private event Action<string> OnSuccess;
        public Popup(string path, Action<string> OnSuccess)
        {
            this.OnSuccess = OnSuccess;
            this.path = path;
            InitializeComponent();
        }

        private void OkClicked(object sender, RoutedEventArgs e)
        {
            bool isFile = (bool)RadioButtonFile.IsChecked;
            bool isDirectory = (bool)RadioButtonDirectory.IsChecked;
            if (isFile && !Regex.IsMatch(PathInputField.Text, "^[a-zA-Z0-9_~-]{1,8}\\.(txt|php|html)$"))
            {
                System.Windows.MessageBox.Show("Wrong name!", "Alert", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else if(!isFile && !isDirectory)
            {
                System.Windows.MessageBox.Show("Specify what do you want to be created!", "Alert", MessageBoxButton.OK, MessageBoxImage.Information);
            }
            else
            {
                string name = PathInputField.Text;
                path = path + "\\" + name;
                FileAttributes attributes = FileAttributes.Normal;
                if ((bool)CheckBoxR.IsChecked)
                {
                    attributes |= FileAttributes.ReadOnly;
                }
                if ((bool)CheckBoxA.IsChecked)
                {
                    attributes |= FileAttributes.Archive;
                }
                if ((bool)CheckBoxH.IsChecked)
                {
                    attributes |= FileAttributes.Hidden;
                }
                if ((bool)CheckBoxS.IsChecked)
                {
                    attributes |= FileAttributes.System;
                }
                if (isFile)
                {
                    File.Create(path);
                }
                else if (isDirectory)
                {
                    Directory.CreateDirectory(path);
                }
                File.SetAttributes(path, attributes);
                OnSuccess(path);
                Close();
            }
        }
        
        private void CancelClicked(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}