# Run the R research pipeline in deterministic file-name order.
#
# Default:
#   Rscript replication/run_all.R
#
# Include collection scripts:
#   Rscript replication/run_all.R --include-collection

args_all <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args_all, value = TRUE)

if (length(file_arg) == 0) {
  stop("Run this file with Rscript: Rscript replication/run_all.R")
}

this_file <- normalizePath(
  sub("^--file=", "", file_arg[[1]]),
  winslash = "/",
  mustWork = TRUE
)

project_root <- normalizePath(
  file.path(dirname(this_file), ".."),
  winslash = "/",
  mustWork = TRUE
)

setwd(project_root)

output_directories <- c(
  "outputs/data",
  "outputs/figures",
  "outputs/tables",
  "outputs/models",
  "outputs/other"
)

for (directory in output_directories) {
  dir.create(directory, recursive = TRUE, showWarnings = FALSE)
}

run_stage <- function(label, relative_directory) {
  scripts <- sort(list.files(
    relative_directory,
    pattern = "^[^_].*\\.[Rr]$",
    full.names = TRUE
  ))

  cat(sprintf("\n=== %s ===\n", label))

  if (length(scripts) == 0) {
    cat(sprintf("No R scripts found in %s; skipping.\n", relative_directory))
    return(invisible(NULL))
  }

  for (script in scripts) {
    cat(sprintf("Running %s\n", script))
    sys.source(script, envir = new.env(parent = globalenv()))
  }

  invisible(NULL)
}

include_collection <- "--include-collection" %in% commandArgs(trailingOnly = TRUE)

if (include_collection) {
  run_stage("DATA COLLECTION", "data/collection")
}

run_stage("DATA CLEANING", "source/cleaning")
run_stage("DATA ANALYSIS", "source/analysis")

cat("\nPipeline completed successfully.\n")
