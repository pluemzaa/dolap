<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="test_interest"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 03:36:55 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xOTswMTozOTowNSBQTTsyNTQ5"/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1BDT007MjU2OC0wNy0xOTswMzozNjo1NSBQTTszOzI2NjM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, e" type="Integer" array="False" size=""/>
            <declare name="interest, in, money" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <assign variable="in" expression="interest/100"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="e" expression="1"/>
            <while expression="e &lt;= year">
                <assign variable="money" expression="money*(1+in)"/>
                <output expression="&quot;Year&quot;&amp;e&amp;&quot;: &quot;&amp;money" newline="True"/>
                <assign variable="e" expression="e+1"/>
            </while>
        </body>
    </function>
</flowgorithm>