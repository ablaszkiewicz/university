using System;
using System.Collections.Generic;

namespace file_explorer
{
    [Serializable]
    public class FileComparer : IComparer<string>
    {
        public int Compare(string x, string y)
        {
            if (x.Length > y.Length)
            {
                return 1;
            }
            if (y.Length > x.Length)
            {
                return -1;
            }
            else
            {
                return string.Compare(x, y, StringComparison.CurrentCulture);
            }
        }
    }
}