from __pyosshell__ import *


def write_xqmp_options(jobfile):
	ofs = open('options.xml','w')
	ofs.write('''<options>
	<xqmultipole>
		<multipoles>system.xml</multipoles> <!-- XML allocation polar sites -> fragment -->
		<control>
''')
	ofs.write('			<job_file>%s</job_file>\n' % jobfile)
	ofs.write('''			<emp_file>mps.tab</emp_file>	<!-- Allocation of .mps files to segs; for template, run 'stateserver' with key = 'emp' -->
			<pdb_check>0</pdb_check>        <!-- Output - Check mapping of polar sites -->
			<!--write_chk></write_chk-->    <!-- Write x y z charge file with dipoles split onto point charges spaced 1fm apart -->
			<format_chk>xyz</format_chk>   	<!-- 'gaussian' or 'xyz' -->
			<split_dpl>1</split_dpl>        <!-- '0' do not split dipoles onto point charges, '1' do split -->
			<dpl_spacing>1e-4</dpl_spacing>	<!-- Spacing a [nm] to be used when splitting dipole onto point charges: d = q * a -->
		</control>
		<coulombmethod>
			<method>cut-off</method>
			<cutoff1>3.0</cutoff1>
			<cutoff2>6.0</cutoff2>
		</coulombmethod>
		<tholemodel>
			<induce>1</induce>
			<induce_intra_pair>1</induce_intra_pair>
			<exp_damp>0.39</exp_damp>
			<scaling>0.25 0.50 0.75</scaling>
		</tholemodel>
		<convergence>
			<wSOR_N>0.30</wSOR_N>
			<wSOR_C>0.30</wSOR_C>
			<max_iter>512</max_iter>
			<tolerance>0.001</tolerance>
		</convergence>
	</xqmultipole>
</options>
''')
	ofs.close()
	return

