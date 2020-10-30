import unittest
import scipy.stats as st
import scipy.special as sp
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) : 
        val = movies_df["runtime"].mean()
        self.assertTrue( np.abs( runtime_mean - val )<1e-6, "you have not set the variable runtime_mean correctly" )  
        val = movies_df["rating"].min()
        self.assertTrue( np.abs( rating_min - val )<1e-6, "you have not set the variable rating_min correctly" )
        val = movies_df["rating"].max()
        self.assertTrue( np.abs( rating_max - val )<1e-6, "you have not set the variable rating_max correctly" )
        val = movies_df["votes"].median()
        self.assertTrue( np.abs( votes_median - val )<1e-6, "you have not set the variable votes_median correctly" )
        val = movies_df["metascore"].quantile(0.25)
        self.assertTrue( np.abs( metascore_p25 - val )<1e-6, "you have not set the variable metascore_p25 correctly" )
        val = movies_df["metascore"].quantile(0.75)
        self.assertTrue( np.abs(metascore_p75 - val )<1e-6, "you have not set the variable metascore_p75 correctly" )
