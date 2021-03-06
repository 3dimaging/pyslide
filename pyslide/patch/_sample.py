# -*- coding: utf-8 -*-

import os, sys
import math, itertools

__all__ = ['wsi_patch_splitting',]

def wsi_patch_splitting(wsi_w, wsi_h, length, overlay=True):
    '''Spltting whole slide image to be patch-wise.
    '''
    coors_arr = []

    # splitting in both w and h direction with overlay
    def split_patch_overlay(ttl_len, sub_len):
        p_sets = []
        if ttl_len < sub_len:
            return p_sets
        if ttl_len == sub_len:
            p_sets.append(0)
            return p_sets

        p_num = int(math.ceil(ttl_len * 1.0 / sub_len))
        overlap_len = (p_num * sub_len - ttl_len) * 1.0 / (p_num - 1)
        extend_len = sub_len - overlap_len
        for ind in range(p_num):
            p_sets.append(int(round(extend_len * ind)))
        return p_sets

    # splitting in both w and h direction with overlay
    def split_patch_no_overlay(ttl_len, sub_len):
        p_sets = []
        if ttl_len < sub_len:
            return p_sets
        if ttl_len == sub_len:
            p_sets.append(0)
            return p_sets

        p_num = int(math.floor(ttl_len * 1.0 / sub_len))
        p_sets = [ele*sub_len for ele in range(p_num)]
        return p_sets

    if overlay == True:
        w_sets = split_patch_overlay(wsi_w, length)
        h_sets = split_patch_overlay(wsi_h, length)
    else:
        w_sets = split_patch_no_overlay(wsi_w, length)
        h_sets = split_patch_no_overlay(wsi_h, length)

    # combine points in both w and h direction
    if len(w_sets) > 0 and len(h_sets) > 0:
        coors_arr = list(itertools.product(w_sets, h_sets))

    return coors_arr
