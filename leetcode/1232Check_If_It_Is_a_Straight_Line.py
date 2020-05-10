class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        a=coordinates[0][1]-coordinates[1][1]
        b=coordinates[0][0]-coordinates[1][0]
        res=[a*x+b*y for x,y in coordinates]
        # for item in coordinates[2:]:
        #     if