﻿/*
    Atlas of Information Management business intelligence library and documentation database.
    Copyright (C) 2020  Riverside Healthcare, Kankakee, IL

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;

namespace Data_Governance_WebApp.Models
{
    public class DpDataInitiative__Metadata
    {
    }
    [ModelMetadataType(typeof(DpDataInitiative__Metadata))]
    public partial class DpDataInitiative
    {
        [NotMapped]
        public virtual string LastUpdatedDateDisplayString
        // don't display the time portion if > 24 hrs ago
        {
            get
            {
                if (LastUpdateDate == null) { return ""; }
                var timeAgo = System.DateTime.Now.Subtract(LastUpdateDate ?? DateTime.Now);
                if (timeAgo.TotalMinutes < 1) { return String.Concat(timeAgo.Seconds.ToString(), " seconds ago"); }
                if (timeAgo.TotalHours < 1) { return String.Concat(timeAgo.Minutes.ToString(), " minutes ago"); }
                else if (timeAgo.TotalHours < 24) { return String.Concat(timeAgo.Hours.ToString(), " hours ago"); }
                else return (LastUpdateDate ?? DateTime.Now).ToShortDateString();
            }
        }
    }
}
