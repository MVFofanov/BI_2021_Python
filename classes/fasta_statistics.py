from statistics import mean
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import os
import time
import datetime


class Fasta(str, object):
    """doc"""

    def __init__(self, path, file_type="fastq"):
        """constructor"""
        self.path = path
        self.file_type = file_type
        self.existence = os.path.exists(path)
        self.line = None
        self.gc_list = []
        self.length_list = []
        self.quality_list = []
        self.list_of_kmers = [''.join(letter) for letter in list(itertools.product('ACTG', repeat=4))]
        self.kmer_dic = {i: 0 for i in self.list_of_kmers}
        self.list_of_kmers = set(self.list_of_kmers)

    def __str__(self):
        return f"Path to the file: {self.path}"

    def calculate_length_and_gc(self, sequence):
        """calculate_length_and_gc"""
        self.line = sequence.strip()
        length = len(self.line)
        gc = (self.line.lower().count('g') + self.line.lower().count('c')) * 100 / length
        return length, gc

    def calculate_quality(self, quality_string):
        """calculate sequence quality"""
        total_quality = 0
        for i in quality_string:
            total_quality += ord(i) - 33  # getting quality for each read letter using Phred+33 quality score
        return total_quality / self.length_list[-1]

    def read_file_fastq(self):
        """read file fastq"""
        number_of_string = 1

        with open(self.path) as file:
            for line in file:
                if line:
                    if number_of_string == 1:
                        if line.strip().startswith(">"):
                            self.file_type = "fasta"
                            self.read_file_fasta()
                            break
                    elif number_of_string == 2:
                        length_and_gc = self.calculate_length_and_gc(line)
                        self.length_list.append(length_and_gc[0])
                        self.gc_list.append(length_and_gc[1])

                        for i in range(len(line.strip()) - 4):
                            word = line.strip()[i: i + 4]
                            if word in self.list_of_kmers:
                                self.kmer_dic[word] += 1
                    elif number_of_string == 4:
                        self.quality_list.append(self.calculate_quality(line))
                    if number_of_string < 4:
                        number_of_string += 1
                    elif number_of_string == 4:
                        number_of_string = 1

    def read_file_fasta(self):
        """read file fasta"""
        number_of_string = 1
        with open(self.path) as file:
            for line in file:
                if line:
                    if number_of_string == 2:
                        length_and_gc = self.calculate_length_and_gc(line)
                        self.length_list.append(length_and_gc[0])
                        self.gc_list.append(length_and_gc[1])

                        for i in range(len(line.strip()) - 4):
                            word = line.strip()[i: i + 4]
                            if word in self.list_of_kmers:
                                self.kmer_dic[word] += 1
                    if number_of_string < 2:
                        number_of_string += 1
                    elif number_of_string == 2:
                        number_of_string = 1

    def get_summary_statistics(self):
        print(f'This {self.file_type} file {self.path} has been successfully parsed')
        print(f'This file contains {len(self.length_list)} sequences')
        print(f'Average sequence length is {round(mean(self.length_list), 2)} bp')
        print(f'Average sequence GC content is {round(mean(self.gc_list), 2)} %')
        if self.file_type == "fastq":
            print(f'Average sequence quality is {round(mean(self.quality_list), 2)}')

    def make_plots(self):
        self.plot_length_histogram()
        self.plot_gc_histogram()
        if self.file_type == "fastq":
            self.plot_quality_histogram()
        self.plot_kmers()

    def get_result(self):
        if self.existence:
            if self.file_type not in {"fastq", "fasta"}:
                print("Wrong file format")
                return
            if self.file_type == "fastq":
                self.read_file_fastq()
            elif self.file_type == "fasta":
                self.read_file_fasta()
            if len(self.length_list) > 0:
                self.get_summary_statistics()
                self.make_plots()
            else:
                print(f'File {self.path} is empty')
        else:
            print(f'File {self.path} is not found')

    def plot_length_histogram(self):
        length_list_df = pd.DataFrame({"Length": self.length_list})
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        fig.set_size_inches(11.7, 8.27)
        length_plot = sns.histplot(x="Length", data=length_list_df, bins=20)
        length_plot.set(title='Length histogram',
                        xlabel='Sequence length (bp)', ylabel='Counts')
        plt.savefig('length_histogram.png', format='png')

    def plot_gc_histogram(self):
        gc_list_df = pd.DataFrame({"GC_content": self.gc_list})
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        fig.set_size_inches(11.7, 8.27)
        gc_plot = sns.histplot(x="GC_content", data=gc_list_df, bins=20)
        gc_plot.set(title='GC content histogram',
                    xlabel='GC content (%)', ylabel='Counts')
        plt.savefig('gc_histogram.png', format='png')

    def plot_quality_histogram(self):
        quality_list_df = pd.DataFrame({"quality": self.quality_list})
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        fig.set_size_inches(11.7, 8.27)
        quality_plot = sns.histplot(x="quality", data=quality_list_df, bins=20)
        quality_plot.set(title='Quality histogram',
                         xlabel='Quality', ylabel='Counts')
        plt.savefig('quality_histogram.png', format='png')

    def plot_kmers(self):
        sns.set_style('whitegrid')
        fig, ax = plt.subplots()
        fig.set_size_inches(20, 14)
        plt.bar(self.kmer_dic.keys(), self.kmer_dic.values())
        plt.xticks(fontsize=5, rotation=90)
        plt.savefig('kmer_histogram.png', format='png')


if __name__ == "__main__":
    start_time = time.process_time()
    path = r"/mnt/c/IB2021-2022/python/SRR1705851.fastq"
    my_file = Fasta(path)
    my_file.get_result()
    my_file2 = Fasta(r"/mnt/c/IB2021-2022/python/amp_res_1_only_one_sequence.fastq")
    print(my_file2)
    end_time = time.process_time()
    total_time = str(datetime.timedelta(seconds=end_time - start_time))
    print(f'Total time for file statistics analysis: {total_time}')
