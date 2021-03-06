# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class genome_wide_association_studies(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def import_gwas_data(self, import_gwas_data_params, context=None):
        """
        :param import_gwas_data_params: instance of type
           "import_gwas_data_params" (Insert your typespec information here.)
           -> structure: parameter "input_shock_id" of String, parameter
           "input_file_path" of String
        :returns: instance of type "Run_import_gwas_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        return self._client.call_method(
            'genome_wide_association_studies.import_gwas_data',
            [import_gwas_data_params], self._service_ver, context)

    def import_snp_data(self, import_snp_data_params, context=None):
        """
        :param import_snp_data_params: instance of type
           "import_snp_data_params" -> structure: parameter "input_shock_id"
           of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_snp_data_result" -> structure:
           parameter "report_ref" of String, parameter "report_name" of String
        """
        return self._client.call_method(
            'genome_wide_association_studies.import_snp_data',
            [import_snp_data_params], self._service_ver, context)

    def import_trait_data(self, import_trait_data_params, context=None):
        """
        :param import_trait_data_params: instance of type
           "import_trait_data_params" -> structure: parameter
           "input_shock_id" of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_trait_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        return self._client.call_method(
            'genome_wide_association_studies.import_trait_data',
            [import_trait_data_params], self._service_ver, context)

    def import_network_data(self, import_network_data_params, context=None):
        """
        :param import_network_data_params: instance of type
           "import_network_data_params" -> structure: parameter
           "input_shock_id" of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_network_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        return self._client.call_method(
            'genome_wide_association_studies.import_network_data',
            [import_network_data_params], self._service_ver, context)

    def import_motif_data(self, import_motif_data_params, context=None):
        """
        :param import_motif_data_params: instance of type
           "import_motif_data_params" -> structure: parameter
           "input_shock_id" of String, parameter "input_file_path" of String
        :returns: instance of type "Run_import_motif_data_result" ->
           structure: parameter "report_ref" of String, parameter
           "report_name" of String
        """
        return self._client.call_method(
            'genome_wide_association_studies.import_motif_data',
            [import_motif_data_params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('genome_wide_association_studies.status',
                                        [], self._service_ver, context)
