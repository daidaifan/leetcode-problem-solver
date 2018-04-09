class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain2times = {}
        for cpdomain in cpdomains:
            times, full_domain = cpdomain.split(' ')
            sub_domains = full_domain.split('.')
            domain = ''
            for i in range(len(sub_domains)):
                if len(domain) == 0:
                    domain = sub_domains[-1]
                else:
                    domain = '%s.%s' % (sub_domains[-i-1], domain)
                domain2times[domain] = domain2times.get(domain, 0) + int(times)
        result = ['%d %s' % (times, domain) for domain, times in domain2times.iteritems()]
        return result
