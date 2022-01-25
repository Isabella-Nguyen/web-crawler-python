
import testingtools
import crawler
import searchdata
import search

output = open('tinyfruits-search-failed.txt', 'w')
success_output = open('tinyfruits-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')



#Test #0 checking search results for 'banana kiwi orange cherry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2697124020714999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09999557120813286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06865223963796284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04489499030467399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04385438269286966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.040870898523307025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03840060984443414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02919422156595541}]
result = search.search('banana kiwi orange cherry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'banana kiwi orange cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'banana kiwi orange cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'banana kiwi orange cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9479235083289533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9463988520887047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8419500965579089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8405400844580355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8365044742736409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6310404395279009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5750094427102465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('banana kiwi orange cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'banana kiwi orange cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'banana kiwi orange cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'peach orange coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22792405480152778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0833205356215853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07368472112043671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04742018708580397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.04679084979612001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04006810309583347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0374860868128804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.020253331160350226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.020253331160350226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach orange coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'peach orange coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'peach orange coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'peach orange coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9996307008705207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8990817156516285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8660821228447964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.810271191685633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7068992384915443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6978664499037553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4377808453791968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4377808453791968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.3933132674209396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach orange coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'peach orange coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'peach orange coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'peach orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27334194193079353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09840042492705912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06947873543551684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04597953285874892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0438667328211387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04382718835015834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'peach orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'peach orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'peach orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.969261310043418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9481904594567137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9473356957737031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8241708325633683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'banana tomato peach cherry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26355949310202514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08814193584219802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0772064179065392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06251414875134181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046035838879308705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.038105276840657995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03528903249146338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03528903249146338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.033525490473738456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana tomato peach cherry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'banana tomato peach cherry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'banana tomato peach cherry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'banana tomato peach cherry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9704482565793638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8236551398206201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8174214219437016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7627813101170681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7627813101170681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.762781310117068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7409011149392807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7246619059919442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana tomato peach cherry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'banana tomato peach cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'banana tomato peach cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'apricot cherry blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2848440328131797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11223255722593851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07558698914880897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04530401755059416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04137726685004367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.040870898523307025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03840060984443414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.029194221565955414}]
result = search.search('apricot cherry blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'apricot cherry blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'apricot cherry blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'apricot cherry blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9792577302641665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9434014125813515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8834347478585991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8722442656452134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8419500965579089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6330927109706134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.631040439527901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('apricot cherry blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'apricot cherry blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'apricot cherry blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'blueberry papaya tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11280229029007091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07723371404100288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02453720402607222}]
result = search.search('blueberry papaya tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'blueberry papaya tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'blueberry papaya tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'blueberry papaya tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9481904594567138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9423856000300839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}]
result = search.search('blueberry papaya tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'blueberry papaya tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'blueberry papaya tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'kiwi blueberry kiwi papaya papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30561146740360506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08695932674470128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07733653334339122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06933885090605547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05717416647689445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0441507211712029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0376947211363917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0376947211363917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02571122758544885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01844049688078277}]
result = search.search('kiwi blueberry kiwi papaya papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'kiwi blueberry kiwi papaya papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'kiwi blueberry kiwi papaya papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'kiwi blueberry kiwi papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9478442886162789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9436401742944325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9307094522518423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8147808750458054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8147808750458054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7309603711775219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5557546489009308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5557546489009308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.4788727327276089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.3985959766206639}]
result = search.search('kiwi blueberry kiwi papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'kiwi blueberry kiwi papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'kiwi blueberry kiwi papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'papaya peach pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10361498692864254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10324408500246525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.051971649598501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04550546180679452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0374612582439532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.022985283089021976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.022985283089021976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.022985283089021976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya peach pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'papaya peach pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'papaya peach pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'papaya peach pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9592677607334981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8678463543864097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8678463543864097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8097345159255595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6341444898718049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4968326732192826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4968326732192826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4968326732192826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya peach pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'papaya peach pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'papaya peach pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'fig pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'fig pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'fig pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'fig pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29546744271304826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1174178179201082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09836736519185915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04592567283238615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.99269496548452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.986987537538252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8238939346789915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'pear apricot apple peach cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2727225109783488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09894537983099169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0886763802185281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04650878067557318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04586567018404988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03741123638272973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02795725599331656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02589102079603921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.024597137120802425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear apricot apple peach cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'pear apricot apple peach cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'pear apricot apple peach cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'pear apricot apple peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9804180008660192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.845840231729698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8287352024552314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8086532808180862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7453935331113173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6043031176618108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5596409243537205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5596409243537205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.531673303388908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear apricot apple peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'pear apricot apple peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'pear apricot apple peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'blueberry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1137004238652347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0400580483740508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'blueberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'blueberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.951275576479978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.865864787505379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'apricot peach coconut lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29146176752337377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07883102564910927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05974533336760692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04534159968444185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04398066443130656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040870898523307025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot peach coconut lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'apricot peach coconut lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'apricot peach coconut lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'apricot peach coconut lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9558135017294763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9506531198566159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9039594425041416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.728996948207601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot peach coconut lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'apricot peach coconut lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'apricot peach coconut lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'apple papaya pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2385500951322192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1087437829066848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10736784290482809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04592030139520683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04318832768324187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03188517299392438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01909948099875674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.019099480998756736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}]
result = search.search('apple papaya pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'apple papaya pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'apple papaya pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'apple papaya pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9680126943577179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.933526561827889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9108035271263045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9025097277104338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7398555660914861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.41284008402077815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4128400840207781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3890545502963912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}]
result = search.search('apple papaya pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'apple papaya pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'apple papaya pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'blueberry apricot pear blueberry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3110338330419366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11935520684774126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11892796096921208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07830468707288572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.051436629287438265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040019395181188105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.036931335994165836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02903580898775024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('blueberry apricot pear blueberry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'blueberry apricot pear blueberry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'blueberry apricot pear blueberry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'blueberry apricot pear blueberry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9996814573859167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9996814573859167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.964661583938166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8650292890229782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7785228096450219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6276163118199057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6276163118199057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6276163118199057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('blueberry apricot pear blueberry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'blueberry apricot pear blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'blueberry apricot pear blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'banana coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2821526758257762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06947873543551684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04597953285874892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'banana coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'banana coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'banana coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9692613100434179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8750875893870586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'banana coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'banana coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'kiwi blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30948479568917386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11473564072080804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10577410203077761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06557266406744591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044596881948494246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04363367322132315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0430732429833672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01762941786812988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'kiwi blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'kiwi blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'kiwi blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.963972816427816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9609894327962026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9598572936406086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9431528176079136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8891131035130447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5255684572228687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5255684572228687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.37163302008004234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'kiwi blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'kiwi blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'banana cherry lime peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30825399412837273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09107093102104817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08078224325709527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05158572692549156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04639549421980224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.042338663451233556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03528903249146338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029916678785502596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029916678785502596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana cherry lime peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'banana cherry lime peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'banana cherry lime peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'banana cherry lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9780298909461547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9560400015745203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9151608558197206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7627813101170681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7627813101170681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6790372088449643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6294355622449899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana cherry lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'banana cherry lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'banana cherry lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'apricot tomato kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3067178104303064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11370042386523471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.08195553289283851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0400580483740508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('apricot tomato kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'apricot tomato kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'apricot tomato kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'apricot tomato kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9523187838800629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9512755764799781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.865864787505379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('apricot tomato kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'apricot tomato kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'apricot tomato kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'coconut fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28487235510929493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04470253788755516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04239520044987674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'coconut fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'coconut fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'coconut fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9662565961159678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8835225885631427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'coconut fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'coconut fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'apricot cherry kiwi blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3063711312724565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10208384478451668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08267389077226897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07534196181460877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.054306663245396555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043597814752710635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03939285333176836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}]
result = search.search('apricot cherry kiwi blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'apricot cherry kiwi blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'apricot cherry kiwi blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'apricot cherry kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.950200362049898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9423777277928652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.858093638351054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8304122780889195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.631040439527901}]
result = search.search('apricot cherry kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'apricot cherry kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'apricot cherry kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'blueberry apricot kiwi papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3063711312724565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0996534628802813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08267389077226897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07534196181460877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07480528573223755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0405830870382606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02654389357899564}]
result = search.search('blueberry apricot kiwi papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'blueberry apricot kiwi papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'blueberry apricot kiwi papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'blueberry apricot kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9502003620498981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.912754552277144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8555027348614265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8376643994720712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.631040439527901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5737529337108416}]
result = search.search('blueberry apricot kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'blueberry apricot kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'blueberry apricot kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'blueberry tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'blueberry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'blueberry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'pear banana pear kiwi pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.276548056568933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11729377548235798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11585705324662357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04730002191887892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04625845469011762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.020844651614259954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.013692393875611952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.007729311556082144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear banana pear kiwi pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'pear banana pear kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'pear banana pear kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'pear banana pear kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9998881290116018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9970975858109754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9859448649494236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9703820293803483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8577050402386264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.1670710126858126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.1670710126858126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.1670710126858126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear banana pear kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'pear banana pear kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'pear banana pear kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'coconut apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.296331499123294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10403039436336696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08268334135819543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04624974494266459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.040310688884251544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04021600395773101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03875592395190091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0356340156425298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02270180269087849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'coconut apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'coconut apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9996998656304898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9190627608556837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.837719040724047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7511749366808564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6950174081593493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.49070517313719036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.49070517313719036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'apple lime blueberry apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31471913333283913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11059252277354831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06983438195818042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05874222615059006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.054185832270632006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04427924653816565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0421417897722862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03650909499096658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03650909499096658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.027114501302786847}]
result = search.search('apple lime blueberry apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'apple lime blueberry apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'apple lime blueberry apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'apple lime blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9760914260911594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9571070471696582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9296156550675824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.88836062096895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7891532678073471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7891532678073471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7167572960253806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5860867631299865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5849106928418828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.43430238308636165}]
result = search.search('apple lime blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'apple lime blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'apple lime blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'kiwi pear apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.25534411625196185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10725775221776636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09276078305165458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0444829828324646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04378025857471177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04346257976741964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04037525155501943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021793846558397497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021738393760375684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.021689469638240078}]
result = search.search('kiwi pear apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'kiwi pear apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'kiwi pear apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'kiwi pear apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9463212968777488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9377136202598353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9015843303725026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.791941690792517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.776934976181073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4926482707130018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4710794730438196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4698808468719355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4688233396708539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.34835493296098957}]
result = search.search('kiwi pear apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'kiwi pear apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'kiwi pear apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'apple coconut pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22534626581869757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.114465109099365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10646425884995278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045993484358950475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04489413917926087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.018653862140027542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.014239751431594309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01420351945859674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.010530044162787728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apple coconut pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'apple coconut pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'apple coconut pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'apple coconut pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9703981062110024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9695554115386195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9587235455112167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8949144051514077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.6989043075899275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3077958075319984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.30701264432575587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.22760955217530612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.22760955217530612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apple coconut pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'apple coconut pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'apple coconut pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2641845659581732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1128022902900709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07723371404100288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04160041608432924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9481904594567137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9423856000300839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8769483134184536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8193600656133992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'pear orange cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.303545817210137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09974783586309117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08285773089971668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045769439068815074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03868454780213231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029412029356386274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02905584246302175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.028030888547907855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear orange cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'pear orange cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'pear orange cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'pear orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9648324746594472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9414377399524093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8384576773541133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.836176227300506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6939901439506108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6357484096820486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6280493404249687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6058947038429281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'pear orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'pear orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'pear apricot coconut papaya pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2624450481105362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11538795584515586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11024223564086556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04724500070073623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.042247285711915855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.028315621286642955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.018295802985931413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017969077092120627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.009999983049204776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear apricot coconut papaya pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'pear apricot coconut papaya pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'pear apricot coconut papaya pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'pear apricot coconut papaya pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9959377232664601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9699249774737935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9233540932280472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9131857030090236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8139650060927717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.395468381702686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.38840611935841657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3454998129737895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.21615214793055323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear apricot coconut papaya pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'pear apricot coconut papaya pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'pear apricot coconut papaya pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'fig orange papaya apricot fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30518675719711985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11154991927863747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07949580288681908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04334390511741573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043340450496177026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.028315621286642955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01933293839353804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.018295802985931413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017969077092120627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig orange papaya apricot fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'fig orange papaya apricot fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'fig orange papaya apricot fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'fig orange papaya apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9465270633597985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9376633128740715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9368894071847996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9368147346781205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6658316983802606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.40754370541073914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.395468381702686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.38840611935841657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3454998129737895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig orange papaya apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'fig orange papaya apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'fig orange papaya apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'cherry papaya coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27062319689076536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10015740084165514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.054612482934615805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.04477649562147291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.044632510854724985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04412558625023501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04359026486967036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.030796521284818554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.017350423358193524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry papaya coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'cherry papaya coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'cherry papaya coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'cherry papaya coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9647429441942628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9188948779125521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8419003876413185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.839329275564235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6663672482738258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6656745508215528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.37503376334984967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.37503376334984967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry papaya coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'cherry papaya coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'cherry papaya coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3084041414467189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9565056787277847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'banana fig lime pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32231808768276415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11655416610757564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11123108689894862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04243740527726817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04058695893087086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03377827358498002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03286698514059547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana fig lime pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'banana fig lime pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'banana fig lime pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'banana fig lime pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9996593423778873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9762208261886689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9349832802274873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9172951852163754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.730125876499352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6928451659658275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4952314688007777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana fig lime pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'banana fig lime pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'banana fig lime pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'pear lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30840414144671885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04616272400490676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'pear lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'pear lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'pear lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9731230302322413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9565056787277846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'pear lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'pear lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'pear lime apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.25534411625196185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11225939300756647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09276078305165458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04535393679790216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04378025857471177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03506096440386093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02279169743866193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021793846558397497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021738393760375684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear lime apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'pear lime apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'pear lime apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'pear lime apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9560735715042484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9463212968777488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9436269880731811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.791941690792517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.776934976181073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4926482707130018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4710794730438196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4698808468719355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4278047273477573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear lime apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'pear lime apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'pear lime apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'fig pear papaya apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27713222984575897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11600780286373588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10317185092963992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.041080432825259146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0388686728095875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.035612024642236326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.028268723588923073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023282654853874117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.023282654853874114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig pear papaya apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'fig pear papaya apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'fig pear papaya apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'fig pear papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9751352708803271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.887963884479054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8641347874342596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8595168351581886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.750711360293095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6110355680539608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5032604386855252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5032604386855251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4742653904820617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig pear papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'fig pear papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'fig pear papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'tomato orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('tomato orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'tomato orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'tomato orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #100 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #100 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #101 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #101 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #102 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #102 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #103 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #103 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking search results for 'orange blueberry peach banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2848440328131797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10262026193127641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0781137086516956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0724023655368019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.044019698628805136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04061991701772503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03963514283469765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021677018651928115}]
result = search.search('orange blueberry peach banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #104 checking search results for 'orange blueberry peach banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #104 checking search results for 'orange blueberry peach banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking search results for 'orange blueberry peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9514968538500184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8595148524659805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8567235779400106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8562791210473024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6566061123923708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.46855420847113666}]
result = search.search('orange blueberry peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #105 checking search results for 'orange blueberry peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #105 checking search results for 'orange blueberry peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking search results for 'peach kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3052997436712434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0437312312088018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #106 checking search results for 'peach kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #106 checking search results for 'peach kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking search results for 'peach kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.946877487331447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9218664874536562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #107 checking search results for 'peach kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #107 checking search results for 'peach kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking search results for 'cherry lime pear cherry lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3080113799343687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10612668961484042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08131063956627088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04016434948512156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03818121167600682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03631325347514977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03276535306048348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03276535306048348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02825290967290458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry lime pear cherry lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #108 checking search results for 'cherry lime pear cherry lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #108 checking search results for 'cherry lime pear cherry lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking search results for 'cherry lime pear cherry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9552875413344724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8920768747491744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8466756310592465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.82529649037918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7082313446810925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7082313446810925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6810321963270841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6106937462830866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.44308483141255894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry lime pear cherry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #109 checking search results for 'cherry lime pear cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #109 checking search results for 'cherry lime pear cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking search results for 'lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #110 checking search results for 'lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #110 checking search results for 'lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking search results for 'lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #111 checking search results for 'lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #111 checking search results for 'lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #112 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #112 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #113 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #113 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking search results for 'fig papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09789197951097454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04691865822383806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03793211738241752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03793211738241752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.027157574678446095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02648542910026186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #114 checking search results for 'fig papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #114 checking search results for 'fig papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking search results for 'fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.819912254592815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.819912254592815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.819912254592815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5724892093031335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #115 checking search results for 'fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #115 checking search results for 'fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking search results for 'fig pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03354352344751557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #116 checking search results for 'fig pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #116 checking search results for 'fig pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking search results for 'fig pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #117 checking search results for 'fig pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #117 checking search results for 'fig pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking search results for 'blueberry papaya pear apricot kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3117084176040702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10882412505544636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0986442028044966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.056376232634112816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05101054457831902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0412498827934999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03751414018616046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02362737565379197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02362737565379197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.018100572084440224}]
result = search.search('blueberry papaya pear apricot kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #118 checking search results for 'blueberry papaya pear apricot kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #118 checking search results for 'blueberry papaya pear apricot kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking search results for 'blueberry papaya pear apricot kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9667537865961331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9147509050654551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.869558974389568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8262126389514719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8108775724026149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6224173375215338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5107116654498053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5107116654498053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4518585607422051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.3912484166795358}]
result = search.search('blueberry papaya pear apricot kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #119 checking search results for 'blueberry papaya pear apricot kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #119 checking search results for 'blueberry papaya pear apricot kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking search results for 'tomato blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #120 checking search results for 'tomato blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #120 checking search results for 'tomato blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking search results for 'tomato blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #121 checking search results for 'tomato blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #121 checking search results for 'tomato blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #122 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #122 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #123 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #123 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking search results for 'peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06762846210478654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06309685343427059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04597953285874892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04382718835015834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #124 checking search results for 'peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #124 checking search results for 'peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking search results for 'peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.969261310043418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9473356957737031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.825184825449364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #125 checking search results for 'peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #125 checking search results for 'peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking search results for 'papaya cherry papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31053073760336725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0835121744271857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07140996007155372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0462388905413633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.044556560092234646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.042422641667479735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02270180269087849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya cherry papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #126 checking search results for 'papaya cherry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #126 checking search results for 'papaya cherry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking search results for 'papaya cherry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.999465245017212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9631012493665345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9631012493665345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8942810568441846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7019843908906209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.49070517313719036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya cherry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #127 checking search results for 'papaya cherry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #127 checking search results for 'papaya cherry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking search results for 'tomato orange fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29546744271304826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11741781792010819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09836736519185915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04592567283238615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04591793916184169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01898944747600852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('tomato orange fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #128 checking search results for 'tomato orange fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #128 checking search results for 'tomato orange fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking search results for 'tomato orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.99269496548452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9925278002512044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9869875375382519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8238939346789915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('tomato orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #129 checking search results for 'tomato orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #129 checking search results for 'tomato orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking search results for 'coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28487235510929493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04616272400490676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04239520044987674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #130 checking search results for 'coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #130 checking search results for 'coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking search results for 'coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9731230302322413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8835225885631427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #131 checking search results for 'coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #131 checking search results for 'coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking search results for 'coconut peach apple kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2841223752281464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10811380839558116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07421295274288325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06159560460359506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05293644979318099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043006368990792264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04189296907885723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04189296907885723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02654441752681524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026476877259438533}]
result = search.search('coconut peach apple kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #132 checking search results for 'coconut peach apple kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #132 checking search results for 'coconut peach apple kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking search results for 'coconut peach apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9065861907793237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9055270598987001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9055270598987001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9055270598987001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9055270598987001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8811965497107296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5737642589746998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5723043591135255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5177586774116921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.42428851480003094}]
result = search.search('coconut peach apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #133 checking search results for 'coconut peach apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #133 checking search results for 'coconut peach apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #134 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #134 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #135 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #135 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking search results for 'pear banana orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29546744271304826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11741781792010819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09836736519185915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04616272400490676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04592567283238615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear banana orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #136 checking search results for 'pear banana orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #136 checking search results for 'pear banana orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking search results for 'pear banana orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.99269496548452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9869875375382519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9731230302322413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8238939346789915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear banana orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #137 checking search results for 'pear banana orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #137 checking search results for 'pear banana orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #138 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #138 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #139 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #139 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking search results for 'banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #140 checking search results for 'banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #140 checking search results for 'banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking search results for 'banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #141 checking search results for 'banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #141 checking search results for 'banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking search results for 'pear peach orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.303545817210137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10000406799693452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09890448871005666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04640967581833456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.044170995559849616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04337702485036556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02786306529444877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.015599488437619373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.015599488437619373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear peach orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #142 checking search results for 'pear peach orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #142 checking search results for 'pear peach orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking search results for 'pear peach orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9783288429780114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9414377399524093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9376052985398916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8376024396424373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.831368692525339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6022671620231688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5389629473534837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear peach orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #143 checking search results for 'pear peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #143 checking search results for 'pear peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #144 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #144 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #145 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #145 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking search results for 'orange kiwi tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04508149302055014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04405772409580497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044026277828701735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('orange kiwi tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #146 checking search results for 'orange kiwi tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #146 checking search results for 'orange kiwi tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking search results for 'orange kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9516390649100088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.950330381086011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}]
result = search.search('orange kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #147 checking search results for 'orange kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #147 checking search results for 'orange kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #148 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #148 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #149 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #149 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking search results for 'blueberry coconut orange tomato apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23690638923989912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10821792163398258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10666440428093198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04731704897725953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04123605518358694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038732724583983275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03597298108768184}]
result = search.search('blueberry coconut orange tomato apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #150 checking search results for 'blueberry coconut orange tomato apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #150 checking search results for 'blueberry coconut orange tomato apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking search results for 'blueberry coconut orange tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9096552966408045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.893387309518794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8913277008828474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7775650309913212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7347576643162789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}]
result = search.search('blueberry coconut orange tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #151 checking search results for 'blueberry coconut orange tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #151 checking search results for 'blueberry coconut orange tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #152 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #152 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #153 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #153 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #154 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #154 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #155 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #155 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #156 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #156 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #157 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #157 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking search results for 'apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #158 checking search results for 'apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #158 checking search results for 'apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking search results for 'apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #159 checking search results for 'apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #159 checking search results for 'apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking search results for 'pear pear banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear pear banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #160 checking search results for 'pear pear banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #160 checking search results for 'pear pear banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking search results for 'pear pear banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear pear banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #161 checking search results for 'pear pear banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #161 checking search results for 'pear pear banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking search results for 'papaya peach apricot lime banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30825399412837273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09107093102104816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08788862046483191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07387479019096496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.044975908273470575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03528903249146338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03343056014848128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029916678785502596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029916678785502596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('papaya peach apricot lime banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #162 checking search results for 'papaya peach apricot lime banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #162 checking search results for 'papaya peach apricot lime banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking search results for 'papaya peach apricot lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9560400015745203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9481046253222599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9014008887912478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.762781310117068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.762781310117068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7387718033496439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7226099631429295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6466565339777288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('papaya peach apricot lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #163 checking search results for 'papaya peach apricot lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #163 checking search results for 'papaya peach apricot lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking search results for 'lime papaya pear tomato banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31092324033350216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11736771111667203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10056844383980085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.051712932480184395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04440711850657906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037669988833599816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.024934382513820297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.024934382513820297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.015599488437619373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime papaya pear tomato banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #164 checking search results for 'lime papaya pear tomato banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #164 checking search results for 'lime papaya pear tomato banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking search results for 'lime papaya pear tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9865663511168603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9643185841550009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9361143792210176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.842329473175459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8142462801024511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6309876911886106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5389629473534838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5389629473534838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime papaya pear tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #165 checking search results for 'lime papaya pear tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #165 checking search results for 'lime papaya pear tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking search results for 'apple pear blueberry cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2699279769899288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10230224132454399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09126619950843515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043933893746727605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03986401639333151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03751414018616046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03703230913781845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02787031385110579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.027651277549156736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02647751654119099}]
result = search.search('apple pear blueberry cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #166 checking search results for 'apple pear blueberry cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #166 checking search results for 'apple pear blueberry cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking search results for 'apple pear blueberry cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9261386699834383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8599294301164494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8371730730567223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8108775724026149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7644168171988963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6024238413978339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5976893166583326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5723181773493412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4518585607422051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3195122524380067}]
result = search.search('apple pear blueberry cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #167 checking search results for 'apple pear blueberry cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #167 checking search results for 'apple pear blueberry cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking search results for 'blueberry tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #168 checking search results for 'blueberry tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #168 checking search results for 'blueberry tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking search results for 'blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #169 checking search results for 'blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #169 checking search results for 'blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking search results for 'tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #170 checking search results for 'tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #170 checking search results for 'tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking search results for 'tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #171 checking search results for 'tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #171 checking search results for 'tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking search results for 'cherry banana papaya cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3096658738771258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11561734630313704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047242204153776605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04443246496114624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04053111329225092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.039514633329679576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03850660448464894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry banana papaya cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #172 checking search results for 'cherry banana papaya cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #172 checking search results for 'cherry banana papaya cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking search results for 'cherry banana papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9958787712806274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9718531816191954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9604189019064939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9604189019064939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8760902046562289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8323299377523474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.48214723197941006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry banana papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #173 checking search results for 'cherry banana papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #173 checking search results for 'cherry banana papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking search results for 'fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #174 checking search results for 'fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #174 checking search results for 'fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking search results for 'fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #175 checking search results for 'fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #175 checking search results for 'fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking search results for 'banana lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #176 checking search results for 'banana lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #176 checking search results for 'banana lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking search results for 'banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #177 checking search results for 'banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #177 checking search results for 'banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking search results for 'cherry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04700050552572875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04166740493176235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #178 checking search results for 'cherry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #178 checking search results for 'cherry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking search results for 'cherry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.990783697140204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9006514341450588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #179 checking search results for 'cherry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #179 checking search results for 'cherry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking search results for 'kiwi fig papaya kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32223126895487125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10125576881510019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0997096539038618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06805446111007687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04805980958195568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03526480836959858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.035233188563902215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.02951552337105723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.022198410898154056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.022198410898154056}]
result = search.search('kiwi fig papaya kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #180 checking search results for 'kiwi fig papaya kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #180 checking search results for 'kiwi fig papaya kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking search results for 'kiwi fig papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9993900768425417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8480862897497163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8381367284676007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7622576996322258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7615742295818481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6221954219746821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5864132400285482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5454601950588398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4798242329683317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4798242329683317}]
result = search.search('kiwi fig papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #181 checking search results for 'kiwi fig papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #181 checking search results for 'kiwi fig papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking search results for 'tomato lime peach banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2757443025730689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10547613571113809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06802182654871261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06727991414163316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045222679397635676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.038718461089473466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('tomato lime peach banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #182 checking search results for 'tomato lime peach banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #182 checking search results for 'tomato lime peach banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking search results for 'tomato lime peach banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9533066290882386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8552122226722418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.836909271533292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8209319342673966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5717760410932535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('tomato lime peach banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #183 checking search results for 'tomato lime peach banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #183 checking search results for 'tomato lime peach banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking search results for 'kiwi cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10085465848703534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04459056362369109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0435528580749021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043467398059126916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}]
result = search.search('kiwi cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #184 checking search results for 'kiwi cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #184 checking search results for 'kiwi cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking search results for 'kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9414059778984581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9399814531880217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}]
result = search.search('kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #185 checking search results for 'kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #185 checking search results for 'kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking search results for 'kiwi pear orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2946253108446575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11157967474451208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08508048523620723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04652743069800276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04323428511260715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03986401639333151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03842256195524182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.027044529874739483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026561569481975557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.019893650534513616}]
result = search.search('kiwi pear orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #186 checking search results for 'kiwi pear orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #186 checking search results for 'kiwi pear orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking search results for 'kiwi pear orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9379134305692569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9137710719378923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.911390725864292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8305133373481788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7126072311577768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5845743131196429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5741350027980512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5677155532481256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.43000625821629446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3195122524380067}]
result = search.search('kiwi pear orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #187 checking search results for 'kiwi pear orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #187 checking search results for 'kiwi pear orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #188 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #188 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #189 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #189 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking search results for 'banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #190 checking search results for 'banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #190 checking search results for 'banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking search results for 'banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #191 checking search results for 'banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #191 checking search results for 'banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking search results for 'pear blueberry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10073578476304852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0963148155965742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043734553104242076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04206919328888758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037669988833599816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0291808765183717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.027634329189106497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.024934382513820293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.024934382513820293}]
result = search.search('pear blueberry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #192 checking search results for 'pear blueberry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #192 checking search results for 'pear blueberry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking search results for 'pear blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.921936513931223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8467621516600996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.814246280102451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8067024285439564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6307519829689987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5389629473534837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5389629473534837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.33718686479947546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.33718686479947546}]
result = search.search('pear blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #193 checking search results for 'pear blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #193 checking search results for 'pear blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking search results for 'blueberry papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1128022902900709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07723371404100288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02453720402607222}]
result = search.search('blueberry papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #194 checking search results for 'blueberry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #194 checking search results for 'blueberry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking search results for 'blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9481904594567137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9423856000300839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}]
result = search.search('blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #195 checking search results for 'blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #195 checking search results for 'blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking search results for 'peach tomato lime apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27410793783761705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11313490114708658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0960031566193375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046339561996830224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04587891117523306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04200126856919941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.026402543163568777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.014781796706548818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.014781796706548818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('peach tomato lime apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #196 checking search results for 'peach tomato lime apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #196 checking search results for 'peach tomato lime apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking search results for 'peach tomato lime apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9768508241670718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9475821444824674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9078679806124715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8501370892625952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8069807532285279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5706976089412839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5598024874686903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('peach tomato lime apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #197 checking search results for 'peach tomato lime apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #197 checking search results for 'peach tomato lime apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking search results for 'coconut blueberry tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2866377966259362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11473564072080805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11166377113686467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04636687542255846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04285653663393014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04151825939286692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.030457382201234822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.021053246683308924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01719309262899024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01719309262899024}]
result = search.search('coconut blueberry tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #198 checking search results for 'coconut blueberry tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #198 checking search results for 'coconut blueberry tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking search results for 'coconut blueberry tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9609894327962027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9386203257634804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9034276831245109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8974276158217795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8889980495222845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4550712205328091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3716330200800424}]
result = search.search('coconut blueberry tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #199 checking search results for 'coconut blueberry tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #199 checking search results for 'coconut blueberry tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
