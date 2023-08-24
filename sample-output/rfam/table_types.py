# This file was generated by db-introspector-gadget
# https://github.com/sesgoe/db-introspector-gadget

# This file requires Python >= 3.10
# If this is in error, please check the --minimum-python-version (-p) argument

import datetime
from typing import Any, TypedDict


class AlignmentAndTree(TypedDict):
    alignment: bytes | None
    average_length: float | None
    number_of_sequences: int | None
    percent_id: float | None
    rfam_acc: str
    tree: bytes | None
    treemethod: str | None
    type: str


class AnnotatedFile(TypedDict):
    cm: bytes
    full: bytes | None
    rfam_acc: str
    seed: bytes


class Author(TypedDict):
    author_id: int
    initials: str | None
    last_name: str | None
    name: str
    orcid: str | None
    synonyms: str | None


class Clan(TypedDict):
    author: str | None
    clan_acc: str
    comment: str | None
    created: datetime.datetime
    description: str | None
    id: str | None
    previous_id: str | None
    updated: datetime.datetime


class ClanDatabaseLink(TypedDict):
    clan_acc: str
    comment: str | None
    db_id: str
    db_link: str
    other_params: str | None


class ClanLiteratureReference(TypedDict):
    clan_acc: str
    comment: str | None
    order_added: bool | None
    pmid: int


class ClanMembership(TypedDict):
    clan_acc: str
    rfam_acc: str


class DatabaseLink(TypedDict):
    comment: str | None
    db_id: str
    db_link: str
    other_params: str | None
    rfam_acc: str


class DbVersion(TypedDict):
    embl_release: str
    genome_collection_date: datetime.datetime | None
    infernal_version: str | None
    number_families: int
    pdb_date: datetime.datetime | None
    refseq_version: int | None
    rfam_release: float
    rfam_release_date: datetime.datetime


class DeadClan(TypedDict):
    clan_acc: str
    clan_id: str
    comment: str | None
    forward_to: str | None
    user: str


class DeadFamily(TypedDict):
    comment: str | None
    forward_to: str | None
    rfam_acc: str
    rfam_id: str
    title: str | None
    user: str


class EnsemblNames(TypedDict):
    ensembl: str | None
    insdc: str


class Family(TypedDict):
    author: str | None
    auto_wiki: int
    clen: int | None
    cmbuild: str | None
    cmcalibrate: str | None
    cmsearch: str | None
    comment: str | None
    created: datetime.datetime
    description: str | None
    ecmli_cal_db: int | None
    ecmli_cal_hits: int | None
    ecmli_lambda: float | None
    ecmli_mu: float | None
    gathering_cutoff: float | None
    hmm_lambda: float | None
    hmm_tau: float | None
    match_pair_node: bool | None
    maxl: int | None
    noise_cutoff: float | None
    number_3d_structures: int | None
    number_of_species: int | None
    num_full: int | None
    num_genome_seq: int | None
    num_pseudonokts: int | None
    num_refseq: int | None
    num_seed: int | None
    previous_id: str | None
    rfam_acc: str
    rfam_id: str
    seed_source: str | None
    structure_source: str | None
    tax_seed: str | None
    trusted_cutoff: float | None
    type: str | None
    updated: datetime.datetime


class FamilyAuthor(TypedDict):
    author_id: int
    desc_order: int
    rfam_acc: str


class FamilyFile(TypedDict):
    cm: bytes
    rfam_acc: str
    seed: bytes


class FamilyLiteratureReference(TypedDict):
    comment: str | None
    order_added: bool | None
    pmid: int
    rfam_acc: str


class FamilyLong(TypedDict):
    reference_sequence: str | None
    referenece_structure: str | None
    rfam_acc: str


class FamilyNcbi(TypedDict):
    ncbi_id: int
    rfam_acc: str
    rfam_id: str | None


class Features(TypedDict):
    database_id: str
    feat_end: int
    feat_orient: bool
    feat_start: int
    primary_id: str
    quaternary_id: str | None
    rfamseq_acc: str | None
    secondary_id: str | None


class FullRegion(TypedDict):
    bit_score: float
    cm_end: int
    cm_start: int
    evalue_score: str
    is_significant: bool
    rfamseq_acc: str
    rfam_acc: str
    seq_end: int
    seq_start: int
    truncated: str
    type: str


class Genome(TypedDict):
    assembly_acc: str | None
    assembly_level: str | None
    assembly_name: str | None
    assembly_version: int | None
    circular: bool | None
    common_name: str | None
    created: datetime.datetime
    description: str | None
    is_reference: bool
    is_representative: bool
    kingdom: str | None
    ncbi_id: int
    num_families: int | None
    num_rfam_regions: int | None
    scientific_name: str | None
    study_ref: str | None
    total_length: int | None
    ungapped_length: int | None
    updated: datetime.datetime
    upid: str
    wgs_acc: str | None
    wgs_version: int | None


class GenomeData(TypedDict):
    author: str
    closed: datetime.datetime | None
    created: datetime.datetime
    data_file: str
    lsf_id: int | None
    message: str | None
    opened: datetime.datetime | None
    status: str
    uuid: str


class GenomeTemp(TypedDict):
    assembly_acc: str | None
    assembly_level: str | None
    assembly_name: str | None
    assembly_version: int | None
    circular: bool | None
    common_name: str | None
    created: datetime.datetime
    description: str | None
    is_reference: bool
    is_representative: bool
    kingdom: str | None
    ncbi_id: int
    num_families: int | None
    num_rfam_regions: int | None
    scientific_name: str | None
    study_ref: str | None
    total_length: int | None
    ungapped_length: int | None
    updated: datetime.datetime
    upid: str
    wgs_acc: str | None
    wgs_version: int | None


class Genseq(TypedDict):
    chromosome_name: str | None
    chromosome_type: str | None
    rfamseq_acc: str | None
    upid: str
    version: str | None


class GenseqTemp(TypedDict):
    chromosome_name: str | None
    chromosome_type: str | None
    rfamseq_acc: str | None
    upid: str
    version: str | None


class HtmlAlignment(TypedDict):
    block: int
    html: bytes | None
    html_alignmentscol: str | None
    rfam_acc: str
    type: str


class Keywords(TypedDict):
    clan_info: str | None
    description: str | None
    literature: str | None
    pdb_mappings: str | None
    rfam_acc: str
    rfam_general: str | None
    rfam_id: str | None
    wiki: str | None


class LiteratureReference(TypedDict):
    author: str | None
    journal: str | None
    pmid: int
    title: str | None


class Lock(TypedDict):
    allowCommits: bool
    alsoAllow: str | None
    locked: bool
    locker: str


class MatchesAndFasta(TypedDict):
    fasta: bytes | None
    match_list: bytes | None
    rfam_acc: str
    type: str


class Motif(TypedDict):
    author: str | None
    average_id: float | None
    average_sqlen: float | None
    clen: int | None
    cmbuild: str | None
    cmcalibrate: str | None
    created: datetime.datetime
    description: str | None
    ecmli_cal_db: int | None
    ecmli_cal_hits: int | None
    ecmli_lambda: float | None
    ecmli_mu: float | None
    gathering_cutoff: float | None
    hmm_lambda: float | None
    hmm_tau: float | None
    match_pair_node: bool | None
    maxl: int | None
    motif_acc: str
    motif_id: str | None
    noise_cutoff: float | None
    num_seed: int | None
    seed_source: str | None
    trusted_cutoff: float | None
    type: str | None
    updated: datetime.datetime
    wiki: str | None


class MotifDatabaseLink(TypedDict):
    comment: str | None
    db_id: str
    db_link: str
    motif_acc: str
    other_params: str | None


class MotifFamilyStats(TypedDict):
    avg_weight_bits: float | None
    frac_hits: float | None
    motif_acc: str
    num_hits: int | None
    rfam_acc: str
    sum_bits: float | None


class MotifFile(TypedDict):
    cm: bytes
    motif_acc: str
    seed: bytes


class MotifLiterature(TypedDict):
    comment: str | None
    motif_acc: str
    order_added: bool | None
    pmid: int


class MotifMatches(TypedDict):
    bit_score: float | None
    e_value: str | None
    motif_acc: str
    motif_start: int | None
    motif_stop: int | None
    query_start: int | None
    query_stop: int | None
    rfamseq_acc: str | None
    rfamseq_start: int | None
    rfamseq_stop: int | None
    rfam_acc: str


class MotifOld(TypedDict):
    author: str | None
    clen: int | None
    cmbuild: str | None
    cmcalibrate: str | None
    created: datetime.datetime
    description: str | None
    ecmli_cal_db: int | None
    ecmli_cal_hits: int | None
    ecmli_lambda: float | None
    ecmli_mu: float | None
    gathering_cutoff: float | None
    hmm_lambda: float | None
    hmm_tau: float | None
    match_pair_node: bool | None
    maxl: int | None
    motif_acc: str
    motif_id: str | None
    noise_cutoff: float | None
    seed_source: str | None
    trusted_cutoff: float | None
    type: str | None
    updated: datetime.datetime


class MotifPdb(TypedDict):
    chain: str | None
    motif_acc: str
    pdb_end: int | None
    pdb_id: str
    pdb_start: int | None


class MotifSsImage(TypedDict):
    image: bytes | None
    motif_acc: str
    rfam_acc: str


class Overlap(TypedDict):
    author: str | None
    auto_overlap: int
    comment: str | None
    description: str | None
    id: str | None


class OverlapMembership(TypedDict):
    auto_overlap: int
    rfam_acc: str


class Pdb(TypedDict):
    author: str | None
    date: str | None
    keywords: str | None
    method: str | None
    pdb_id: str
    resolution: float | None
    title: str | None


class PdbFullRegion(TypedDict):
    bit_score: float
    chain: str | None
    cm_end: int
    cm_start: int
    evalue_score: str
    hex_colour: str | None
    is_significant: bool
    pdb_end: int
    pdb_id: str
    pdb_start: int
    rfam_acc: str


class PdbFullRegionOld(TypedDict):
    bit_score: float
    chain: str | None
    cm_end: int
    cm_start: int
    evalue_score: str
    hex_colour: str | None
    is_significant: bool
    pdb_end: int
    pdb_id: str
    pdb_start: int
    rfam_acc: str


class PdbRfamReg(TypedDict):
    auto_pdb_reg: int
    chain: str | None
    hex_colour: str | None
    pdb_id: str
    pdb_res_end: int | None
    pdb_res_start: int | None
    pdb_seq: str
    rfamseq_acc: str | None
    rfam_acc: str
    seq_end: int | None
    seq_start: int | None


class PdbSequence(TypedDict):
    chain: str | None
    pdb_id: str
    pdb_seq: str


class PostProcess(TypedDict):
    author: str
    closed: datetime.datetime | None
    created: datetime.datetime
    lsf_id: int | None
    message: str | None
    opened: datetime.datetime | None
    rfam_acc: str
    status: str
    uuid: str


class ProcessedData(TypedDict):
    cm: bytes | None
    genome_full: str | None
    genome_full_md5: str | None
    refseq_full: str | None
    refseq_full_md5: str | None
    rfam_acc: str
    scores_graph: bytes | None
    ss_stats_fam: bytes | None
    ss_stats_pbp: bytes | None
    ss_stats_seq: bytes | None


class Pseudoknot(TypedDict):
    covariation: bool | None
    pseudoknot_id: str
    rfam_acc: str
    source: str


class Refseq(TypedDict):
    description: str | None
    ncbi_taxid: int | None
    refseq_acc: str
    species: str | None


class RefseqFullRegion(TypedDict):
    bit_score: float
    cm_end: int
    cm_start: int
    evalue_score: str
    refseq_acc: str
    rfam_acc: str
    seq_end: int
    seq_start: int
    truncated: str


class Rfamseq(TypedDict):
    accession: str
    description: str
    length: int | None
    mol_type: str
    ncbi_id: int
    previous_acc: str | None
    rfamseq_acc: str
    source: str
    version: int


class RfamseqTemp(TypedDict):
    accession: str
    description: str | None
    length: int | None
    mol_type: str
    ncbi_id: int
    previous_acc: str | None
    rfamseq_acc: str
    source: str
    version: int


class RnacentralMatches(TypedDict):
    md5: str
    rfamseq_acc: str
    rnacentral_id: str | None
    seq_end: int
    seq_start: int
    type: str | None


class RscapeAnnotations(TypedDict):
    alen: int | None
    avgid: float | None
    F: float | None
    found: int | None
    nseq: int | None
    ppv: float | None
    rfam_acc: str
    sensitivity: float | None
    tp: int | None
    true: int | None


class SecondaryStructureImage(TypedDict):
    image: bytes | None
    rfam_acc: str
    type: str | None


class SeedRegion(TypedDict):
    md5: str | None
    rfamseq_acc: str | None
    rfam_acc: str
    seq_end: int
    seq_start: int


class Sunburst(TypedDict):
    data: bytes
    rfam_acc: str
    type: str


class TaxonomicTree(TypedDict):
    level: str | None
    lft: int | None
    ncbi_code: int
    parent: str | None
    rgt: int | None
    species: str | None
    taxonomy: str | None


class Taxonomy(TypedDict):
    align_display_name: str | None
    ncbi_id: int
    species: str
    tax_string: str | None
    tree_display_name: str | None


class TaxonomyWebsearch(TypedDict):
    level: str | None
    lft: int | None
    minimal: bool
    ncbi_id: int | None
    parent: int | None
    rank: str | None
    rgt: int | None
    species: str | None
    taxonomy: str | None


class Version(TypedDict):
    embl_release: str
    number_families: int
    rfam_release: float
    rfam_release_date: datetime.date


class Wikitext(TypedDict):
    auto_wiki: int
    title: str