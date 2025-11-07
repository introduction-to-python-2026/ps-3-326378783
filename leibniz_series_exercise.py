def approximate_pi(n_terms):
   list_of_numbers = []
   for i in range(n_terms):
      list_of_numbers.append(((-1)**i)/(2*i+1))
   leibniz_series = sum(list_of_numbers)
   phi = leibniz_series*4
   return phi
