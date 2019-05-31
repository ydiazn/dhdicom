# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-


import os
import numpy as np
from copy import deepcopy
from dhdicom.helpers import utils
from dhdicom.helpers.blocks_class import BlocksImage


class DataHiding():
    def process(self, data, msg):
        pass


class EPRHindingAndAuthentication():
    """
    A novel hash function based fragile watermarking method for image integrity
    """

    def __init__(self, key, x0=0.57, p=0.45, n=512):
        # Hash of key
        self.sha512_key = utils.sha512_to_key_bin(key)
        self.x0 = x0
        self.p = p
        self.n = n

    def get_msg(self, watermarked_array):
        # Initial Values
        x = self.x0
        modified_blocks = []
        extracted_lsb = ""
        # Red
        # square_color = (255, 0, 0)
        # Green
        square_color = (0, 255, 0)
        # Blue
        # square_color = (0, 0, 255)
        if len(watermarked_array.shape) == 2:
            red_watermarked_array = watermarked_array
        else:
            # Red component
            red_watermarked_array = watermarked_array[:, :, 0]
        # Instance
        block_instace_32x32 = BlocksImage(red_watermarked_array, 32, 32)
        # Convert to integer sequence
        int_seq = list(map(int, self.sha512_key))
        # Calculating chaotic positions
        x = utils.pwlcm(x, self.p)
        pos = utils.random_list(x, self.p, list(range(1024)))[:self.n]
        # Watermark extraction process
        for i in range(block_instace_32x32.max_num_blocks()):
            block3x32 = block_instace_32x32.get_block(i)
            block_instace_1x1 = BlocksImage(block3x32, 1, 1)
            copy_1x1 = deepcopy(block_instace_1x1)
            for j in range(self.n):
                copy_1x1.set_block([[int_seq[j]]], pos[j])
            hash_seq = utils.sha256_to_image_bin(copy_1x1.get())
            for j in range(256, self.n):
                extracted_lsb += utils.ext_lsb(
                    block_instace_1x1.get_block(pos[j])[0][0]
                )

        return utils.bin2char(extracted_lsb)

    def authenticate(self, watermarked_array):
        # Initial Values
        x = self.x0
        modified_blocks = []
        # Red
        # square_color = (255, 0, 0)
        # Green
        square_color = (0, 255, 0)
        # Blue
        # square_color = (0, 0, 255)
        if len(watermarked_array.shape) == 2:
            red_watermarked_array = watermarked_array
        else:
            # Red component
            red_watermarked_array = watermarked_array[:, :, 0]
        # Instance
        block_instace_32x32 = BlocksImage(red_watermarked_array, 32, 32)
        # Convert to integer sequence
        int_seq = list(map(int, self.sha512_key))
        # Calculating chaotic positions
        x = utils.pwlcm(x, self.p)
        pos = utils.random_list(x, self.p, list(range(1024)))[:self.n]
        # Watermark extraction process
        for i in range(block_instace_32x32.max_num_blocks()):
            block3x32 = block_instace_32x32.get_block(i)
            block_instace_1x1 = BlocksImage(block3x32, 1, 1)
            copy_1x1 = deepcopy(block_instace_1x1)
            for j in range(self.n):
                copy_1x1.set_block([[int_seq[j]]], pos[j])
            hash_seq = utils.sha256_to_image_bin(copy_1x1.get())
            extracted_lsb = ""
            for j in range(256):
                extracted_lsb += utils.ext_lsb(
                    block_instace_1x1.get_block(pos[j])[0][0]
                )
            if extracted_lsb != hash_seq:
                modified_blocks.append(i)

        if modified_blocks:
            return False, modified_blocks

        return True,

    def process(self, cover_array, msg=None):
        # Initial value
        x, l = self.x0, 0
        bin_msg = utils.char2bin(msg)
        if len(cover_array.shape) == 2:
            red_cover_array = cover_array
        else:
            # Red component
            red_cover_array = cover_array[:, :, 0]
        # Instance
        block_instace_32x32 = BlocksImage(red_cover_array, 32, 32)
        # Convert to integer sequence
        int_seq = list(map(int, self.sha512_key))
        # Calculating chaotic positions
        x = utils.pwlcm(x, self.p)
        pos = utils.random_list(x, self.p, list(range(1024)))[:self.n]
        # Watermark insertion process
        for i in range(block_instace_32x32.max_num_blocks()):
            block3x32 = block_instace_32x32.get_block(i)
            block_instace_1x1 = BlocksImage(block3x32, 1, 1)
            copy_1x1 = deepcopy(block_instace_1x1)
            for j in range(self.n):
                copy_1x1.set_block([[int_seq[j]]], pos[j])
            hash_seq = utils.sha256_to_image_bin(copy_1x1.get())
            r = 0
            for j in range(self.n):
                if j < 256:
                    coef = utils.replace(
                        block_instace_1x1.get_block(pos[j])[0][0], hash_seq[r]
                    )
                    r += 1
                else:
                    if l < len(bin_msg):
                        coef = utils.replace(
                            block_instace_1x1.get_block(pos[j])[0][0],
                            bin_msg[l]
                        )
                        l += 1
                block_instace_1x1.set_block([[coef]], pos[j])

        return cover_array
