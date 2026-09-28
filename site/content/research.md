---
title: Our Research
subtitle: Computational Biology & Evolutionary Genomics
description: Clade-scale genomics of Drosophilidae: genome atlases, natural selection at amino-acid resolution, parallel adaptation, and the Hawaiian Drosophila radiation.
---
# Research

## Overview
We study how natural selection shapes genomes, from single amino acids to entire evolutionary radiations. Our work is deliberately end-to-end: we collect flies in the field, generate long-read genomic data at the bench, and build the computational methods needed to analyze thousands of genomes at once. Most of our work uses the fly family Drosophilidae, which pairs a century of *Drosophila melanogaster* genetics with more than 4,500 species of varied, often convergent ecologies. Small genomes and high genetic diversity make it one of the few clades where population genomics at the scale of a whole lineage is feasible.

## From Model Species to Model Clade
We lead an international effort to sequence every drosophilid species. By solving the problem of assembling high-quality genomes from a single small insect, we cut the cost of a reference genome to a few hundred dollars and have released hundreds of assemblies, including single-fly genomes from wild-caught specimens. Combined with automated, low-cost population resequencing, the result is a growing atlas of reference genomes and polymorphism data at comparable scales across the clade.

We use this resource to infer a time-calibrated Drosophilidae Tree of Life, to map ancestral gene flow between lineages, and to develop genome-skimming tools that identify species from low-coverage sequencing. All data, workflows, and metadata are released openly for the community.

* Single-fly long-read (Nanopore) genome assembly and chromosome-scale scaffolding.
* Comparative annotation and orthology across hundreds of species.
* Phylogenomics, introgression, and low-cost genomic species identification.

## Natural Selection at Amino-Acid Resolution
Polymorphisms are sparse within any one species, so classic estimates of selective constraint average over thousands of sites and blur the details of how selection acts. We take an evolutionary replication approach that pools polymorphism across orthologous positions in many species, so that the density of variants grows with every genome we add. With 150+ species, nearly every conserved residue is covered by at least one nonsynonymous variant.

We are building hierarchical Bayesian models that estimate the distribution of fitness effects (DFE) jointly across species and smooth those estimates across 3D protein structures. This lets us ask where in a protein constraint and adaptation occur, connect those maps to biochemistry and function, and test them against experimental measurements of enzyme activity.

* Multi-species DFE inference and McDonald-Kreitman-style tests in 3D.
* Selection across proteins, domains, tissues, and cell types.
* Links between molecular evolution and protein structure and stability.

## Is Adaptation Repeatable?
Adaptation is pervasive in *Drosophila*, but how often does it use the same genes, pathways, or nucleotides? Existing answers come mostly from a literature biased toward conspicuous traits and large-effect variants. Clade-scale sampling lets us measure parallelism systematically and ask how it depends on relatedness, shared ecology, and population size.

To scan hundreds of species for recent selection, we are developing a cost-effective approach that combines pooled long-read sequencing with deep learning, alongside classic summary statistics and machine-learning methods we have previously developed for detecting adaptive introgression. Insecticide resistance, which evolves repeatedly across insects, is a focal test case.

* Scalable selective sweep detection from long-read pool-seq data.
* Parallel adaptation across nucleotides, genes, pathways, and lineages.

## The Hawaiian *Drosophila* Radiation
More than 700 endemic species of Hawaiian *Drosophila* arose from a single ancestor within a few million years, many of them living side by side. Adaptive radiation is usually explained as a response to ecological opportunity, but repeated bottlenecks, isolation, and relaxed constraint on islands suggest that chance plays a large role. Are these flies adaptive agents or random wanderers? Together with collaborators in Hawaiʻi and on the mainland, we are building the Hawaiian Drosophila Genomics Project to find out.

* **A genomic atlas of the radiation:** field surveys across the islands, annotated genomes and population genomic data for hundreds of species, compared against the mainland drosophilids we have already sequenced.
* **Biogeography and speciation:** a time-calibrated phylogeny anchored to island ages, ancestral reconstruction of host and habitat shifts, and tests of whether sympatric speciation is linked to abrupt barriers such as large inversions.
* **Selection across scales:** measuring constraint and adaptation at the level of genes, species, and lineages to separate directed from random change.
* **Behavioral evolution:** as part of a multi-institution team, linking genomes, gene regulation, and neurochemistry to the remarkable diversity of courtship, aggression, and sleep behaviors across the radiation.
* **Conservation:** many of these species are threatened by habitat loss. We are developing cost-efficient genomic tools for field monitoring, assessing extinction risk, and guiding captive breeding with state and university partners.

## Field and Laboratory Methods
Good genomics starts long before the computer. We run collecting expeditions for non-model drosophilids, maintain live cultures, and develop the molecular protocols that turn a single tiny fly into a near telomere-to-telomere genome. Standardized wet-lab protocols on liquid-handling robots, containerized Snakemake workflows, and a lightweight relational database tie the field, the bench, and the computer into one reproducible pipeline.
