
def findingValleyHelper(A:[],lst):
       N = len(A)
       ans = base = 0

       while base < N:
           end = base
           if end + 1 < N and A[end] > A[end + 1]: #if base is a left-boundary
               #set end to the peak of this potential mountain
               while end+1 < N and A[end] > A[end+1]:
                   end += 1

               if end + 1 < N and A[end] < A[end + 1]: 
                   while end+1 < N and A[end] < A[end+1]:
                       end += 1
                   
                   ans = max(ans, end - base + 1)

           base = max(end, base + 1)

       lst.append(ans)

def findingValley(A):
       lst = []
       for i in range(len(A)):
              j = i+1
              
              while j < len(A):
                     findingValleyHelper((A[0:i]+(A[j:])),lst)
                     j+=1 
       return max(lst)
       
                     
              
       
