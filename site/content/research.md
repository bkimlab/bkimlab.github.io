---
title: Our Research
subtitle: Clade-scale genomics of Drosophilidae
description: Clade-scale genomics of Drosophilidae
---
# Research

## Overview
We study how evolution shapes genomes, from single amino acids to entire evolutionary radiations, using clade-scale genome sequencing. Our work is intentionally end-to-end: we collect flies in the field (and collaborate extensively with local experts), generate new datasets, and build the computational methods needed to analyze thousands of genomes at once. Our work currently focuses on the dipteran family Drosophilidae, where we can connect broad sequencing efforts to mechanistic understanding from a century of *Drosophila melanogaster* genetics. Small genomes and high genetic diversity currently make it one of the few systems where population genomics at the scale of a whole lineage is feasible.

## From Model Species to Model Clade
We are part of an international effort to sequence every drosophilid species. By developing inexpensive approaches to assembling high-quality genomes from single flies, we've cut the cost of a reference genome to a few hundred dollars, allowing us to release hundreds of genomes. We are working on hundreds (eventually thousands) more. Combined with lab automation for low-cost population resequencing, the result is a growing atlas of reference genomes and polymorphism data at comparable scales across the clade. This provides us with tools and resources to support our own projects, but releasing open resources to share with our community is field a top priority too.

* Single-fly long-read (Nanopore) genome assembly and chromosome-scale scaffolding.
* Comparative annotation and orthology across hundreds of species.
* A genomic Drosophilidae Tree of Life.
* Phylogenomics, introgression.
* Low-cost species identification with genome skimming.

## Natural Selection at Amino-Acid Resolution
Polymorphisms are sparse within any one species, so classic population genetic estimates of purifying selection average over many thousands of sites and obscure the details of how selection acts in connection to function. We take an evolutionary replication approach that pools polymorphisms across orthologous positions in many species. With 150+ species, at least one nonsynonymous variant exists for nearly every neutral residue (codon) of an ortholog, allowing us to study natural selection very precisely with population genomic data.

We are building hierarchical Bayesian models that estimate the distribution of fitness effects (DFE) jointly across across 3D protein structures, genes, to lineages. This lets us ask where in a protein constraint and adaptation occur, connect those maps to biochemistry and function, and ultimately to test them against computational predictions of fitness effects or experimental measurements of enzyme activity.

* Multi-species DFE inference and McDonald-Kreitman-style tests in 3D.
* Selection across proteins, domains, tissues, and cell types.
* Links between molecular evolution and protein structure and stability.

## Is Adaptation Repeatable?
Adaptation is pervasive in *Drosophila*, but how often does it use the same genes, pathways, or nucleotides? Existing answers come mostly from a literature biased toward conspicuous traits and large-effect variants. Clade-scale sampling lets us measure parallelism systematically and ask how it depends on phylogenetic relatedness, shared ecology, and population size.

To scan hundreds of species for recent selection, we are developing a cost-effective approaches for detecting recent selection in sampled species, alongside classic summary statistics and machine-learning methods.

* Scalable selective sweep detection with deep learning.
* Parallel adaptation across nucleotides, genes, pathways, and lineages.

## The Hawaiian *Drosophila* and *Scaptomyza* Radiation
More than 700 endemic species of Hawaiian Drosophilidae arose from a single ancestor within a few million years-one of Earth's great radiations. Adaptive radiation is usually explained as a response to ecological opportunity, but repeated bottlenecks, isolation, and relaxed constraint on islands suggest that chance plays a large role. Can we use genomic data to disentangle these processes? Together with [Sam Church's lab](https://shchurch.github.io/) and other collaborators in Hawaiʻi and on the mainland, we are building the Hawaiian *Drosophila* Genomes Project to find out.

* **A genomic atlas of the radiation:** field surveys across the islands, annotated genomes and population genomic data for hundreds of species, compared against the mainland drosophilids we have already sequenced.
* **Biogeography and speciation:** phylogenies anchored to island ages, ancestral reconstruction of host and habitat shifts, and tests of whether sympatric speciation is linked to abrupt barriers such as large inversions.
* **Selection across scales:** measuring constraint and adaptation at the level of genes, species, and lineages.
* **Conservation genomics:** many of these species are threatened by habitat loss. We are using short- and long-read sequencing of fresh and museum wild-collected specimens to understand the genomic diversity of populations over time, understand the importance of specific types of variation (e.g. TEs) for conservation, and (potentially) assess extinction risk.