<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="work5"/>
        <attribute name="authors" value="nitis"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-20 01:22:14 AM"/>
        <attribute name="created" value="bml0aXM7TUVMSUtFQ0hFUlJZOzI1NjgtMDctMTk7MDk6NTE6NTMgUE07Mjc1Ng=="/>
        <attribute name="edited" value="bml0aXM7TUVMSUtFQ0hFUlJZOzI1NjgtMDctMjA7MDE6MjI6MTQgQU07MTQ7Mjg4MA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="interest" type="Real" array="False" size=""/>
            <declare name="year, i, money" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="i" expression="0"/>
            <while expression="i &lt; year">
                <assign variable="i" expression="i+1"/>
                <assign variable="money" expression="money * (1 + interest/100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot;&amp;money&amp;&quot;&quot;" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>