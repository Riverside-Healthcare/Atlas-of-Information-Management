﻿using System;
using System.Collections.Generic;

namespace Data_Governance_WebApp.Models
{
    public partial class SharedItems
    {
        public int Id { get; set; }
        public int? SharedFromUserId { get; set; }
        public int? SharedToUserId { get; set; }
        public string Url { get; set; }
        public string Name { get; set; }
        public DateTime? ShareDate { get; set; }

        public virtual User SharedFromUser { get; set; }
        public virtual User SharedToUser { get; set; }
    }
}
