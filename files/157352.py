<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4.Money"/>
        <attribute name="authors" value="akung"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 06:24:18 PM"/>
        <attribute name="created" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNTo0MjoxNSBQTTsyMTk0"/>
        <attribute name="edited" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNjoxMzo0NCBQTTsxO2FrdW5nO0tJRERPOzI1NjgtMDctMTc7MDQ6NTQ6MjQgUE07bGFiNC5SYWJiaXRWZW5kZXIuZnByZzs2NzAz"/>
        <attribute name="edited" value="YWt1bmc7S0lERE87MjU2OC0wNy0xNzswNjoyNDoxOCBQTTszOzIzMDg="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="mon, inter, year, i" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="inter"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt; year">
                <assign variable="i" expression="i+1"/>
                <assign variable="mon" expression="mon*(1+(inter/100))"/>
                <output expression="&quot;Year &quot; &amp;i&amp; &quot;:&quot;" newline="False"/>
                <output expression="mon" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>