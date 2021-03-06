﻿using System;
using System.Collections.Generic;

namespace Data_Governance_WebApp.Models
{
    public partial class MailRecipients
    {
        public int Id { get; set; }
        public int? MessageId { get; set; }
        public int? ToUserId { get; set; }
        public DateTime? ReadDate { get; set; }
        public int? AlertDisplayed { get; set; }
        public int? ToGroupId { get; set; }

        public virtual MailMessages Message { get; set; }
        public virtual UserGroups ToGroup { get; set; }
        public virtual User ToUser { get; set; }
    }
}
