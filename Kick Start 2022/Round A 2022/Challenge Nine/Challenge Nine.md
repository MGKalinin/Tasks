## [Challenge Nine ](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997)
# Explanations
First, let us decide which digit to insert. In fact, a number is a multiple of 9 if and only if the sum of its all digits is a multiple of 9. Therefore, we can add up all the L digits of the given N, and use **9 − (sum mod 9)** to get the new digit we want. Wherever we insert it, the sum of all digits of the new number and the new number itself will be a multiple of 9. Note that when **sum mod 9 = 0**, adding either a new 0 or a new 9 can make the result be a multiple of 9, but 0 is always more preferable than 9 because we are looking for the smallest answer.


Secondly, let us decide where to insert the new digit. Let us use d to represent the new digit we are going to insert. We can start from the most significant digit aL−1, then aL−2, and then use this order to visit all the digits in N, to find the first digit in N that is larger than d. Then we should insert d right before this digit.


Note that there are some edge cases. For example, all digits in N are less than d. In this case, we should append d to the end of N. And if d is 0, we will find that the first digit in N that is larger than d is the leading digit. Be careful that we should not put d before it because the result cannot have leading zeros. In this case, we should put 0 right after the leading digit of N to get the smallest result.


*(Во-первых, давайте решим, какую цифру вставить. На самом деле число кратно 9 тогда и только тогда, когда сумма всех его цифр кратна 9.Следовательно, мы можем сложить все цифры L данного N и использовать **9-(sum mod 9)**, чтобы получить новую цифру, которую мы хотим.Куда бы мы его ни вставляли, сумма всех цифр нового числа и самого нового числа будет кратна 9. Обратите внимание, что когда **sum mod 9=0**, добавление либо нового 0, либо нового 9 может привести к тому, что результат будет кратно 9, но 0 всегда предпочтительнее 9, потому что мы ищем наименьший ответ.)*

*(Во-вторых, давайте решим, куда вставить новую цифру. Давайте использовать d для представления новой цифры, которую мы собираемся вставить. Мы можем начать со старшей цифры aL-1, затем aL-2, а затем использовать этот порядок для посещения всех цифр в N, чтобы найти первую цифру в N, которая больше, чем d. Затем мы должны вставить d прямо перед этой цифрой.)*

*(Обратите внимание, что есть некоторые крайние случаи. Например, все цифры в N меньше d. В этом случае мы должны добавить d в конец N. И если d равно 0, мы обнаружим, что первая цифра в N, которая больше d, является старшей цифрой. Будьте осторожны, мы не должны ставить d перед ним, потому что результат не может иметь ведущих нулей. В этом случае мы должны поставить 0 сразу после первой цифры N, чтобы получить наименьший результат.)*