'''
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径
'''


class Solution:
    # O(n) 44ms 86.48%
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split('/')
        st = []
        for one in pathArr:
            if one in ('', '.'):
                continue
            elif one == '..':
                if len(st) == 0:
                    continue
                st.pop()
            else:
                st.append(one)
        return '/' + '/'.join(st)


if __name__ == "__main__":
    path = '/home/aaa/..//bbb/./ccc'
    path = '/a/./b/../../c/'
    path = ""
    res = Solution().simplifyPath(path)
    print(res)
