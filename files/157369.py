<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab3"/>
        <attribute name="authors" value=""/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-17 10:52:16 PM"/>
        <attribute name="created" value="Z3V5eGE7REVTS1RPUC1TT0JKOEQ5OzI1NjgtMDctMTc7MTA6NTA6MzUgUE07MjkxOA=="/>
        <attribute name="edited" value="Z3V5eGE7REVTS1RPUC1TT0JKOEQ5OzI1NjgtMDctMTc7MTA6NTI6MTYgUE07MTszMDI3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, rate, years, i" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="rate"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="i" expression="1"/>
            <while expression="i &lt;= years">
                <assign variable="money" expression="money * (1 + rate / 100)"/>
                <output expression="&quot;Year &quot; &amp; i &amp; &quot;: &quot; &amp; money" newline="True"/>
                <assign variable="i" expression="i + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>