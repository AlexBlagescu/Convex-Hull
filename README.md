# Convex_Hull

Given a set of points in the plane. the convex hull of the set is the smallest convex polygon that contains all the points of it.

Let points[0..n-1] be the input array:

        1. Find the bottom-most point by comparing y coordinate of all points. If there are two points with the same y value, then the point with smaller x coordinate value is considered. Let the bottom-most point be P0. Put P0 at first position in output hull.

        2. Consider the remaining n-1 points and sort them by polar angle in counterclockwise order around points[0]. If the polar angle of two points is the same, then put the nearest point first.

        3. After sorting, check if two or more points have the same angle. If two more points have the same angle, then remove all same angle points except the point farthest from P0. Let the size of the new array be m.

        4. If m is less than 3, return (Convex Hull not possible)

        5. Create an empty stack ‘S’ and push points[0], points[1] and points[2] to S.

        6. Process remaining m-3 points one by one. Do following for every point ‘points[i]’
                4.1. Keep removing points from stack while orientation of following 3 points is not counterclockwise (or they don’t make a left turn).
                         4.1.1. Point next to top in stack
                         4.1.2. Point at the top of stack 
                         4.1.3. points[i]
                4.2. Push points[i] to S

        5. Print contents of S
# Time Complexity:

Let n be the number of input points. The algorithm takes O(nLogn) time if we use a O(nLogn) sorting algorithm.
The first step (finding the bottom-most point) takes O(n) time. The second step (sorting points) takes O(nLogn) time. The third    step takes O(n) time. In the third step, every element is pushed and popped at most one time. So the sixth step to process points one by one takes O(n) time, assuming that the stack operations take O(1) time. Overall complexity is O(n) + O(nLogn) + O(n) + O(n) which is O(nLogn).
