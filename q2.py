class Codec:

    def compressed_data(self, data):
        temp = []
        c = 0
        for i in range(0, len(data) - 1):
            if data[i] == data[i + 1]:
                c = c + 1
            else:
                temp.append([data[i], c + 1])
                c = 0
        temp.append([data[-1], (c + 1)])

        comp = ''
        for i in temp:
            comp = comp + i[0]
        return [comp, temp]

    def decompress(self, compress_data):
        dec = ''
        for i in compress_data[1]:
            for j in range(i[1]):
                dec = dec + i[0]
        return dec


s = "       3@@@8m mm"
c = Codec()
compressed_string = c.compressed_data(s)
print(compressed_string[0])
decompressed_string = c.decompress(compressed_string)
print(decompressed_string)


# OUTPUT:-
# ' 3@8m m'
# "       3@@@8m mm"
