 public List<List<String>> solveNQueens(int n) {
            List<List<String>> res = new ArrayList<>();
            solve(res, new int[n], n, 0, new String[n]);
            return res;
        }

        public void solve(List<List<String>> list, int[] c, int n, int index, String[] cur) {
            if(index == n) {
                list.add(Arrays.asList(cur.clone()));
                return;
            }
            // 从第一列开始遍历
            for(int j=0;j<n;j++) {
                c[index] = j; // 将第index行的皇后放在第j列
                boolean has = false; // 是否有冲突标志位
                // 遍历当前已放置好的皇后，看是否有冲突
                for(int i=0;i<index;i++) {
                    if(c[i] == c[index] || Math.abs(i-index)==Math.abs(c[i]-c[index])) {
                        has = true;
                    }
                }
                if(!has) {
                    char[] row = new char[n];
                    Arrays.fill(row, '.');
                    row[j] = 'Q';
                    cur[index] = new String(row);
                    // 如果没有冲突，当前解法可行，增加一位皇后
                    solve(list, c, n, index+1, cur);
                }
            }
        }
