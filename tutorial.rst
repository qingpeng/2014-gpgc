=======================================
Running the Big GPGC script pipeline
=======================================

:Date: January, 2014

 
 corn/ prairie all convert to fasta format
 and combine them together to have two fasta files
 
get processed data from Adina
details about preprocessing to be added 
including: quality filtering

HPCC: /mnt/research/adina/gpgc-trimmed-reads/iowa-corn/
/mnt/research/adina/gpgc-trimmed-reads/iowa-prairie



Iowa Corn:

/mnt/research/adina/gpgc-trimmed-reads/iowa-corn

-rwxrwxrwx 1 howead mmg  9302977703 Oct 18 12:31 1424.1.1371.qc.fastq.gz.fq.all.fa (for some reason I only have fastaon this one)
-rwxrwxrwx 1 howead mmg 18057840674 Jan 20  2012 1424.2.1371.qc.fastq
-rwxrwxrwx 1 howead mmg 17939571834 Jan 20  2012 1424.3.1371.qc.fastq
-rwxrwxrwx 1 howead mmg  7233040797 Jan 20  2012 1424.4.1371.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  3332956027 Jan 20  2012 1424.5.1371.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  6896082071 Jan 20  2012 1424.6.1371.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7007160578 Jan 20  2012 1424.7.1371.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  5226754822 Jan 20  2012 1425.1.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7692674484 Jan 20  2012 1425.2.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7622998438 Jan 20  2012 1425.3.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7322276736 Jan 20  2012 1425.4.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7259815677 Jan 20  2012 1425.5.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7270277913 Jan 20  2012 1425.6.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg  7132146580 Jan 20  2012 1425.7.1367.qc.fastq.gz
-rwxrwxrwx 1 howead mmg 50542777929 Jan 20  2012 iowa-corn-all-reads-minus-649-30min-70N.fasta (only fasta)

Iowa Prairie

/mnt/research/adina/gpgc-trimmed-reads/iowa-prairie

-rwxrwxrwx 1 howead mmg  17G Jan 23  2012 1461.1.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  17G Jan 23  2012 1461.2.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  17G Jan 23  2012 1461.3.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  16G Jan 23  2012 1461.4.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  18G Jan 23  2012 1461.5.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  17G Jan 23  2012 1461.6.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  17G Jan 23  2012 1461.7.1405.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg 9.5G Jan 23  2012 GPCZ.1427-1.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  12G Jan 23  2012 GPCZ.1427-2.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  12G Jan 23  2012 GPCZ.1427-3.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  11G Jan 23  2012 GPCZ.1427-4.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  12G Jan 23  2012 GPCZ.1427-5.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  12G Jan 23  2012 GPCZ.1427-6.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg  12G Jan 23  2012 GPCZ.1427-7.1377.fastq.bz2-trimmed.fq.bz2.gz
-rwxrwxrwx 1 howead mmg 1.6G Apr 16  2012 GPCZ.604-2.778.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.1G Apr 16  2012 GPCZ.850-1.1039.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.2G Apr 16  2012 GPCZ.850-2.1039.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.2G Apr 16  2012 GPCZ.850-3.1039.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.2G Apr 16  2012 GPCZ.850-4.1039.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.3G Apr 16  2012 GPCZ.850-5.1039.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.2G Apr 16  2012 GPCZ.850-6.1039.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.1G Apr 16  2012 GPCZ.895-1.1070.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 2.9G Apr 16  2012 GPCZ.895-2.1070.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 3.0G Apr 16  2012 GPCZ.895-3.1070.fastq.bz2.trimmed.gz
-rwxrwxrwx 1 howead mmg 9.5G Apr 16  2012 GPCZ.895-4.1070.fastq.bz2.trimmed (unzipped already)

preprocess prairie data:
1. gzip -d *.gz
2. cat 1461.* GPCZ.* > iowa-prairie-all.fastq (size: 607209331246)
3. fastq-to-fasta.py iowa-prairie-all.fastq >iowa-prairie-all.fasta (prairie-fastq-to-fasta.qsub)

preprocess corn data:
1. gzip -d *.gz
2. cat 142*.fastq >all_142.fastq
3. fastq-to-fasta.py all_142.fastq >all_142.fasta
4. cat all_142.fasta iowa-corn-all-reads-minus-649-30min-70N.fasta 1424.1.1371.qc.fastq.gz.fq.all.fa >iowa-corn-all.fasta

Finally only keep two final files to save storage space.
iowa-prairie-all.fasta and iowa-corn-all.fasta


Older:
use smaller iowa-corn data and use iowa prairie *.fastq file

Newer:
full data set,
only iowa-corn-all.fasta older version missing 1424.1.1371.qc.fastq.gz.fq.all.fa

Small data set testing:
- get the increase of coverage 
- smaller hash table
- original smaller corn file


Installing necessary software
-----------------------------

Before we get started, we need to install all the necessary software, including:

 - MetaSim


wget http://ab.inf.uni-tuebingen.de/data/software/metasim/download/V0_9_5/MetaSim_unix_0_9_5.sh
bash MetaSim_unix_0_9_5.sh -c

./bin/MetaSim



echo 'export PATH=$PATH:/home/qingpeng/bin/metasim/' >> ~/.bashrc
source ~/.bashrc
 
 
================




Before we get started, we need to install all the necessary software, including:

 - Tallymer
 - Jellyfish
 - DSK
 - ipython
 - LaTex
 - Velvet
