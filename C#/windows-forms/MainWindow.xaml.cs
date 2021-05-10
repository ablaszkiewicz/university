using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace windows_forms
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void OpenClicked(object sender, RoutedEventArgs e)
        {
            FolderBrowserDialog folderBrowserDialog = new FolderBrowserDialog()
            {
                Description = "Select directory to open"
            };
            DialogResult dialogResult = folderBrowserDialog.ShowDialog();
            if (dialogResult == System.Windows.Forms.DialogResult.OK)
            {
                TreeView.Items.Clear();
                DirectoryInfo directoryInfo = new DirectoryInfo(folderBrowserDialog.SelectedPath);
                TreeViewItem rootTreeViewItem = CreateTreeViewDirectory(directoryInfo);
                TreeView.Items.Add(rootTreeViewItem);
            }
        }

        private void ExitClicked(object sender, RoutedEventArgs e)
        {
            Close();
        }
        
        private void CreateClicked(object sender, RoutedEventArgs e)
        {
            TreeViewItem selectedTreeViewItem = (TreeViewItem) TreeView.SelectedItem;
            Popup popup = new Popup((string)selectedTreeViewItem.Tag, OnCreationSuceed);
            popup.ShowDialog();
        }

        private void OnCreationSuceed(string path)
        {
            TreeViewItem currentTreeViewItem = (TreeViewItem)TreeView.SelectedItem;
            if (File.Exists(path))
            {
                FileInfo file = new FileInfo(path);
                currentTreeViewItem.Items.Add(CreateTreeViewFile(file));
            }
            else if (Directory.Exists(path))
            {
                DirectoryInfo dir = new DirectoryInfo(path);
                currentTreeViewItem.Items.Add(CreateTreeViewDirectory(dir));
            }
        }

        private void DeleteClicked(object sender, RoutedEventArgs e)
        {
            TreeViewItem treeViewItem = (TreeViewItem)TreeView.SelectedItem;
            string path = (string)treeViewItem.Tag;
            FileAttributes attributes = File.GetAttributes(path);
            File.SetAttributes(path, attributes & ~FileAttributes.ReadOnly);
            if((attributes & FileAttributes.Directory) == FileAttributes.Directory)
            {
                RemoveDirectory(path);
            }
            else
            {
                File.Delete(path);
            }
            if ((TreeViewItem) TreeView.Items[0] != treeViewItem)
            {
                TreeViewItem parent = (TreeViewItem)treeViewItem.Parent; 
                parent.Items.Remove(treeViewItem);
            }
            else
            {
                TreeView.Items.Clear();
            }
        }

        private void OpenFileClicked(object sender, RoutedEventArgs e)
        {
            TreeViewItem treeViewItem = (TreeViewItem) TreeView.SelectedItem;
            string fileContent = File.ReadAllText((string) treeViewItem.Tag);
            ScrollViewer.Content = new TextBlock() {Text = fileContent};
        }

        private TreeViewItem CreateTreeViewFile(FileInfo fileInfo)
        {
            TreeViewItem treeViewItem = new TreeViewItem
            {
                Header = fileInfo.Name,
                Tag = fileInfo.FullName,
            };
            treeViewItem.ContextMenu = new ContextMenu();
            MenuItem openMenuItem = new MenuItem {Header = "Open"};
            openMenuItem.Click += OpenFileClicked;
            MenuItem deleteMenuItem = new MenuItem {Header = "Delete"};
            deleteMenuItem.Click += DeleteClicked;
            treeViewItem.ContextMenu.Items.Add(openMenuItem);
            treeViewItem.ContextMenu.Items.Add(deleteMenuItem);
            treeViewItem.Selected += StatusBarUpdate;
            
            return treeViewItem;
        }

        private TreeViewItem CreateTreeViewDirectory(DirectoryInfo directoryInfo)
        {
            TreeViewItem rootTreeViewItem = new TreeViewItem
            {
                Header = directoryInfo.Name,
                Tag = directoryInfo.FullName
            };
            
            rootTreeViewItem.ContextMenu = new ContextMenu();
            MenuItem createMenuItem = new MenuItem {Header = "Create"};
            createMenuItem.Click += CreateClicked;
            MenuItem deleteMenuItem = new MenuItem {Header = "Delete"};
            deleteMenuItem.Click += DeleteClicked;
            rootTreeViewItem.ContextMenu.Items.Add(createMenuItem);
            rootTreeViewItem.ContextMenu.Items.Add(deleteMenuItem);
            rootTreeViewItem.Selected += StatusBarUpdate;
            
            foreach (DirectoryInfo subdirectoryInfo in directoryInfo.GetDirectories())
            {
                rootTreeViewItem.Items.Add(CreateTreeViewDirectory(subdirectoryInfo));
            }

            foreach (FileInfo subfileInfo in directoryInfo.GetFiles())
            {
                rootTreeViewItem.Items.Add(CreateTreeViewFile(subfileInfo));
            }

            return rootTreeViewItem;
        }
        
        private void StatusBarUpdate(object sender, RoutedEventArgs e)
        {
            TreeViewItem treeViewItem = (TreeViewItem)TreeView.SelectedItem;
            Console.WriteLine($"Clicked object with tag: {treeViewItem.Tag}");
            FileAttributes fileAttributes = File.GetAttributes((string)treeViewItem.Tag);
            StatusText.Text = "";
            if((fileAttributes & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
            {
                StatusText.Text += 'r';
            }
            else
            {
                StatusText.Text += '-';
            }
            if ((fileAttributes & FileAttributes.Archive) == FileAttributes.Archive)
            {
                StatusText.Text += 'a';
            }
            else
            {
                StatusText.Text += '-';
            }
            if ((fileAttributes & FileAttributes.Hidden) == FileAttributes.Hidden)
            {
                StatusText.Text += 'h';
            }
            else
            {
                StatusText.Text += '-';
            }
            if ((fileAttributes & FileAttributes.System) == FileAttributes.System)
            {
                StatusText.Text += 's';
            }
            else
            {
                StatusText.Text += '-';
            }
        }

        private void RemoveDirectory(string path)
        {
            DirectoryInfo directoryInfo = new DirectoryInfo(path);
            foreach(DirectoryInfo subdirectoryInfo in directoryInfo.GetDirectories())
            {
                RemoveDirectory(subdirectoryInfo.FullName);
            }
            foreach(var file in directoryInfo.GetFiles())
            {
                File.Delete(file.FullName);
            }
            Directory.Delete(path);
        }
    }
}