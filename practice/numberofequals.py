def main():
    n, m = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    i = j = res = 0

    while i < n and j < m:
       if nums1[i] == nums2[j] :
           disi = i
           disj = j
           while i < n and nums1[i] == nums1[disi] : i += 1
           while j < m and nums2[j] == nums2[disj] : j += 1
           res += (i - disi)*(j - disj)
       elif nums1[i] > nums2[j] :
            j += 1
       else:
           i += 1
           

    print(res)
main()
