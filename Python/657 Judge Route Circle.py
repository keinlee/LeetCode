#判断路线成圆

# runtime:32ms
class Solution(object):
    def judgeCircle(self,moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')


#另一种方法 runtime:33ms
class Solution(object):
    def judgeCircle(self,moves):
        """
        :type moves: str
        :rtype: bool
        """
        c=collections.Counter(moves)
        return c['U']==c['D'] and c['L']==c['R']
