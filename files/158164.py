<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test4fc"/>
        <attribute name="authors" value="News"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 09:53:41 PM"/>
        <attribute name="created" value="TmV3cztERVNLVE9QLU9HTzgySEw7MjU2OC0wNy0yMTswOTo0OTowNSBQTTsyNzgx"/>
        <attribute name="edited" value="TmV3cztERVNLVE9QLU9HTzgySEw7MjU2OC0wNy0yMTswOTo1Mzo0MSBQTTsxOzI4ODQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, per, i, total" type="Integer" array="False" size=""/>
            <declare name="mon" type="Real" array="False" size=""/>
            <output expression="&quot;input money:&quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;input interest(%):&quot;" newline="True"/>
            <input variable="per"/>
            <output expression="&quot;input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <output expression="&quot;Year&quot;&amp;(i+1)&amp;&quot;:&quot;" newline="False"/>
                <assign variable="mon" expression="mon*(1+(per/100))"/>
                <output expression="mon" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>