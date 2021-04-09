from decimal import Decimal

def num2hypercase(num):

	format_HyperNum_int = ['元','拾','佰','仟','万','拾','佰','仟','亿','拾','佰','仟']

	format_HyperNum_dec = ['分', '角']

	format_num_dict = {'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}

	res = []

	if int(num) == num:

		num = str(int(num))

		k = len(num) - 1

		for i in num:

			res.append(format_num_dict[i])

			if i != '0':

				res.append(format_HyperNum_int[k])

			elif i == '0' and res[-2] == '零':

				res = res[:-1]

			k = k - 1

		if res[-1] == '零':

			res = res[:-1]

		if res[-1] != '元':
		
			res.append('元')


	elif int(num) != num:

		float_num = Decimal(float(num)).quantize(Decimal('0.00'))

		part_split = str(float_num).split('.')

		int_part = part_split[0]
		dec_part = part_split[1]

		k = len(int_part) - 1

		for i in int_part:

			res.append(format_num_dict[i])

			if i != '0':

				res.append(format_HyperNum_int[k])

			elif i == '0' and res[-2] == '零':

				res = res[:-1]

			k = k - 1

		if res[-1] == '零':

			res = res[:-1]

		if res[-1] != '元':

			res.append('元')

		m = len(dec_part) - 1

		for j in dec_part:

			res.append(format_num_dict[j])

			if j != '0':

				res.append(format_HyperNum_dec[m])

			m = m - 1

		if res[-1] == '零':

			res = res[:-1]

	else:

		res = '***'

	raw_res = ''.join(res)

	if '角' not in raw_res and '分' not in raw_res:

		raw_res = raw_res + ' 整'

	return raw_res


if __name__ == "__main__":

	print('输入金额：')

	while 1:

		raw_typed_input = input()

		if raw_typed_input == 's':

			break

		typed_input = float(raw_typed_input)

		hypercase_input = num2hypercase(typed_input)

		print(typed_input, '    ', hypercase_input)

		


