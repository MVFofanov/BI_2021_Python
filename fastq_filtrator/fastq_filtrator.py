def greeting_message():
    text = '''
            This program can help you to filter your raw .fastq data obtained from Illumina sequencing.

            The following parameters are subject to change:

            Input .fastq file name                                 input format: my_reads.fastq
            Output .fastq file prefix                              input format: my_result
            GC content (%)                default: 0, 100          input format: 40, 60
            Read length (bp)              default: 0, 2**32        input format: 100, 150
            Read quality                  default: 0               input format: 30

            You can save reads failed after filtering by typing 'yes' or 'y' when you will be asked about it.
            Type one number as upper boundary instead using interval for GC content and Read length.
            Skip the output .fastq file prefix step and use input fastq name as output prefix.
            Skip all steps except Input .fastq file name to use default settings.

            After filtering you can get:
            no output file                every single read was saved and nothing was filtered
            *_passed.fastq file           contains all reads saved after filtering
            *_failed.fastq file           contains all reads discarded after filtering

            WARNING!
            Make sure available RAM have at least three times the size of the .fastq file before RUN,
            This program is sensitive to it, dont use it to analyse whole human genome raw sequencing data.
            '''
    return text


# This program is sensitive to RAM because it was realised through dictionaries containing information about reads:
# header, sequence, quality line from input *.fastq file and calculated Read length, Read GC content and Read quality
# for each individual read. In addition, reads that have passed the filtering and\
# those that have been eliminated after filtering are also stored in the RAM in the dictionaries in the same manner.
# This script for tested on the .fastq data which took up about 100 Mb disk space.
# After RUN, this program demanded usage up to 300 Mb RAM and time up to 10 seconds


def calculate_length(value):
    return len(value[0][:-1])


def calculate_gc(value):
    return (value[0].lower().count('g') + value[0].lower().count('c')) * 100 / value[2]


def calculate_quality(value):
    total_quality = 0
    for i in value[1][:-1]:
        total_quality += ord(i) - 33
    return total_quality / value[2]


def calculate_reads_number(fastq_dic):
    return len(fastq_dic)


def calculate_total_reads_length(fastq_dic):
    total_reads_length = 0
    for value in fastq_dic.values():
        total_reads_length += value[2]
    return total_reads_length


def calculate_average_reads_length(reads_number, total_reads_length):
    return total_reads_length / reads_number


def calculate_average_gc(fastq_dic, reads_number):
    total_gc = 0
    for value in fastq_dic.values():
        total_gc += value[3]
    return total_gc / reads_number


def calculate_average_quality(fastq_dic, reads_number):
    total_quality = 0
    for value in fastq_dic.values():
        total_quality += value[4]
    return total_quality / reads_number


def calculate_and_print_statistics(fastq_dic):
    reads_number = (len(fastq_dic))
    average_gc = calculate_average_gc(fastq_dic, reads_number)
    average_quality = calculate_average_quality(fastq_dic, reads_number)
    total_reads_length = calculate_total_reads_length(fastq_dic)
    average_reads_length = calculate_average_reads_length(reads_number, total_reads_length)

    statistics = {'Total reads_number': f'{reads_number} reads',
                  'Total reads length': f'{total_reads_length} bp',
                  'Average reads length': f'{average_reads_length} bp',
                  'Average GC content': f'{average_gc} %',
                  'Average quality': average_quality
                  }
    for i in statistics:
        print(f'{i} is {statistics[i]}')
    print()


def read_file_and_generate_dictionary_with_fastq_data(input_fastq):
    with open(input_fastq) as r:
        fastq_file = r.readlines()

        fastq_dic = {}

        for i in range(0, len(fastq_file), 4):
            fastq_dic[fastq_file[i]] = [fastq_file[i + 1], fastq_file[i + 3]]

        for key, value in fastq_dic.items():
            fastq_dic[key].append(calculate_length(value))
            fastq_dic[key].append(calculate_gc(value))
            fastq_dic[key].append(calculate_quality(value))

    return fastq_dic


def write_to_file(fastq_dic, name):
    with open(name, 'w') as w:
        for key, value in fastq_dic.items():
            read = [key, value[0], '+\n', value[1]]
            w.writelines(read)


def save_filtered_or_not(save_filtered, fastq_dic_passed, fastq_dic_failed):
    if save_filtered:
        return fastq_dic_passed, fastq_dic_failed
    else:
        return fastq_dic_passed, {}


def filter_by_length(length_bounds, fastq_dic, fastq_dic_failed, save_filtered):
    fastq_dic_passed = {}
    for key, value in fastq_dic.items():
        if int(length_bounds[0]) <= value[2] <= int(length_bounds[1]):
            fastq_dic_passed[key] = value
        else:
            if key not in fastq_dic_failed:
                fastq_dic_failed[key] = value
    return save_filtered_or_not(save_filtered, fastq_dic_passed, fastq_dic_failed)


def filter_by_gc(gc_bounds, fastq_dic, fastq_dic_failed, save_filtered):
    fastq_dic_passed = {}
    for key, value in fastq_dic.items():
        if float(gc_bounds[0]) <= value[3] <= float(gc_bounds[1]):
            fastq_dic_passed[key] = value
        else:
            if key not in fastq_dic_failed:
                fastq_dic_failed[key] = value
    return save_filtered_or_not(save_filtered, fastq_dic_passed, fastq_dic_failed)


def filter_by_quality(quality_threshold, fastq_dic, fastq_dic_failed, save_filtered):
    fastq_dic_passed = {}
    for key, value in fastq_dic.items():
        if value[4] >= quality_threshold:
            fastq_dic_passed[key] = value
        else:
            if key not in fastq_dic_failed:
                fastq_dic_failed[key] = value
    return save_filtered_or_not(save_filtered, fastq_dic_passed, fastq_dic_failed)


def filter_reads(gc_bounds, length_bounds, quality_threshold, save_filtered, fastq_dic):
    if len(gc_bounds) != 2:
        gc_bounds = tuple(f'0, {gc_bounds[0]}'.split(', '))

    if len(length_bounds) != 2:
        length_bounds = tuple(f'0, {length_bounds[0]}'.split(', '))

    fastq_dic_failed = {}
    fastq_dic_passed = fastq_dic

    if gc_bounds != (0, 100):
        fastq_dic_passed, fastq_dic_failed = filter_by_gc(gc_bounds, fastq_dic_passed, fastq_dic_failed, save_filtered)

    if length_bounds != (0, 2**32):
        fastq_dic_passed, fastq_dic_failed =\
            filter_by_length(length_bounds, fastq_dic_passed, fastq_dic_failed, save_filtered)

    if quality_threshold != 0:
        fastq_dic_passed, fastq_dic_failed =\
            filter_by_quality(quality_threshold, fastq_dic_passed, fastq_dic_failed, save_filtered)

    return fastq_dic_passed, fastq_dic_failed


def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2**32),
         quality_threshold=0, save_filtered=False):

    if output_file_prefix.strip() == '':
        passed = input_fastq[:-6] + '_passed.fastq'
        failed = input_fastq[:-6] + '_failed.fastq'
    else:
        passed = output_file_prefix + '_passed.fastq'
        failed = output_file_prefix + '_failed.fastq'

    fastq_dic = read_file_and_generate_dictionary_with_fastq_data(input_fastq)

    print('Sequencing quality statistics without any filtering')
    calculate_and_print_statistics(fastq_dic)

    fastq_dic_passed, fastq_dic_failed =\
        filter_reads(gc_bounds, length_bounds, quality_threshold, save_filtered, fastq_dic)

    if len(fastq_dic) != len(fastq_dic_passed):
        if save_filtered:

            print('Sequencing quality statistics after filtering')
            if len(fastq_dic_passed) != 0:
                calculate_and_print_statistics(fastq_dic_passed)
                write_to_file(fastq_dic_passed, passed)
            else:
                print('After filtering, not a single read was left. Try again!')

            print('Sequencing quality statistics after filtering for failed reads')
            if len(fastq_dic_failed) != 0:
                calculate_and_print_statistics(fastq_dic_failed)
                write_to_file(fastq_dic_failed, failed)

        else:
            print('Sequencing quality statistics after filtering')
            if len(fastq_dic_passed) != 0:
                calculate_and_print_statistics(fastq_dic_passed)
                write_to_file(fastq_dic_passed, passed)
            else:
                print('After filtering, not a single read was left. Try again!')
    else:
        print('After filtering, every single read was saved and nothing was filtered. Try again!')


if __name__ == '__main__':
    print(greeting_message())

    try:
        input_fastq = input('Type your input .fastq file name with its extension *.fastq: ')

        output_file_prefix = input('Type your output .fastq file name prefix without any extension: ')

        gc_input_text = 'Type allowable interval for GC content to filter .fastq file with it: 40, 60, for example: '
        gc_bounds = input(gc_input_text)
        if gc_bounds == '':
            gc_bounds = (0, 100)
        else:
            gc_bounds = tuple(gc_bounds.split(', '))

        length_input_text = 'Type allowable interval for Read length to filter .fastq with it: 100, 150, for example: '
        length_bounds = input(length_input_text)
        if length_bounds == '':
            length_bounds = (0, 2**32)
        else:
            length_bounds = tuple(length_bounds.split(', '))

        quality_thresh_input_text = 'Type allowable Read quality threshold to filter .fastq with it: 30, for example: '
        quality_threshold = input(quality_thresh_input_text)
        if quality_threshold == '':
            quality_threshold = 0
        else:
            quality_threshold = int(quality_threshold)

        save_filtered = input('Type "yes" to save reads removed after filtering or "no" to discard: ').lower()
        print()
        if save_filtered in {'yes', 'y'}:
            save_filtered = True
        else:
            save_filtered = False

        if input_fastq == '':
            print('Input *.fastq file name is empty. Try again!')
        else:
            main(input_fastq, output_file_prefix, gc_bounds, length_bounds,
                 quality_threshold, save_filtered)
    except ValueError:
        print('Wrong input format. Try again!')
