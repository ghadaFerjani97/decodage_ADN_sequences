#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Projet_Bioinfo as projet

sequences_dic=projet.read_fasta('regulatory_seqs_MET.fasta')

lst=[0,0,0,0]
for key in sequences_dic :
        t=projet.nucleotide_count(sequences_dic[key])
        for i in range(4):
            lst[i]+=t[i]

nb_necleotide=sum(lst)
print(nb_necleotide)