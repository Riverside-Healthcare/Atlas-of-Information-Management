﻿using System;
using System.Collections.Generic;

namespace Data_Governance_WebApp.Models
{
    public partial class DpReportAnnotation
    {
        public int ReportAnnotationId { get; set; }
        public string Annotation { get; set; }
        public int? ReportId { get; set; }
        public int? DataProjectId { get; set; }
        public int? Rank { get; set; }

        public virtual DpDataProject DataProject { get; set; }
        public virtual ReportObject Report { get; set; }
    }
}
