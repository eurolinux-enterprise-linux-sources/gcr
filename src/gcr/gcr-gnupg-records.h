/*
 * Copyright (C) 2011 Collabora Ltd.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as
 * published by the Free Software Foundation; either version 2.1 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
 * 02111-1307, USA.
 *
 * Author: Stef Walter <stefw@collabora.co.uk>
 */

#if !defined (__GCR_H_INSIDE__) && !defined (GCR_COMPILATION)
#error "Only <gcr/gcr.h> can be included directly."
#endif

#ifndef GCR_GNUPG_RECORDS_H
#define GCR_GNUPG_RECORDS_H

#include <gio/gio.h>

#include "gcr-record.h"

G_BEGIN_DECLS

const gchar *       _gcr_gnupg_records_get_keyid             (GPtrArray *records);

const gchar *       _gcr_gnupg_records_get_short_keyid       (GPtrArray *records);

const gchar *       _gcr_gnupg_records_get_fingerprint       (GPtrArray *records);

gchar *             _gcr_gnupg_records_get_user_id           (GPtrArray *records);

gboolean            _gcr_gnupg_records_parse_user_id         (const gchar *user_id,
                                                              gchar **name,
                                                              gchar **email,
                                                              gchar **comment);

GIcon *             _gcr_gnupg_records_get_icon              (GPtrArray *records);

G_END_DECLS

#endif /* __GCR_GNUPG_RECORD_H__ */
