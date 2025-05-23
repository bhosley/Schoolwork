pkgs <- c('xtable','survival','actuar',
          'knitcitations','knitr','stringr',
          'DT','shape')

IMG <- function(path, img_name) {
  
  return(file.path(path, img_name))
  
  }

lapply(X = pkgs,
       FUN = function(x) {
  
        if(!x%in%installed.packages())  install.packages(x)

        do.call('library', args = list(x))
})


# package options
options("DT.options" = list(columnDefs = list(list(className = 'dt-right', 
                                                   targets   = "_all"))))

knitcitations::cite_options(cite.style = "numeric", citation_format = 'pandoc')

knitr::knit_hooks$set(
  
  jkf_par = function(before, options, envir) {
  
  if (before) {
    
    par(cex.lab = 1.05, 
        cex.axis = 1.05, 
        mgp = c(3.25,0.7, 0), 
        tcl = -0.3, 
        font.lab = 2, 
        font = 2, 
        font.axis = 2, 
        tck = 0.015, 
        family = "serif",
        lwd = 2)  }
})

knitr::knit_hooks$set(
  
  source = function(x, options){
  if (!is.null(options$verbatim) && options$verbatim){
    opts = gsub(",\\s*verbatim\\s*=\\s*TRUE\\s*", "", options$params.src)
    bef = sprintf('\n\n    ```{r %s}\n', opts, "\n")
    stringr::str_c(
      bef, 
      knitr:::indent_block(paste(x, collapse = '\n'), "    "), 
      "\n    ```\n"
    )
  } else {
    stringr::str_c("\n\n```", tolower(options$engine), "\n", 
                   paste(x, collapse = '\n'), "\n```\n\n"
    )
  }
})

knitr::knit_hooks$set(
  
  latex = function(before, options, envir) {
  
  if (before) {
    
    if(output=='pdf') '\\vspace{7px}'
  }
})

knitr::opts_chunk$set(message = FALSE, 
                      warning = FALSE, 
                      echo = FALSE, 
                      results = "asis", 
                      jkf_par = TRUE,
                      fig.align = 'center',
                      fig.pos = 'h',
                      fig.width = 8,
                      fig.height = 6,
                      comment = NA)
                      #out.width = '100%'
                      

getYAML <- function(file) {
  
  lines  <- readLines(file)
  header <- list(lines[min(which(lines%in%'---'))+1:max(which(lines%in%'---'))-1])
  header <- unlist(header)
  header <- header[-c(1,length(header))]
  output <- header[which(header%in%'output:')+1]
  output <- gsub(" ", "", unlist(strsplit(output, ':'))[1])
  output <- gsub('_document', '', output)
  
  yaml <- list()
  
  yaml$output <- output

  invisible(yaml)  
}

