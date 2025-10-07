<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab_404"/>
        <attribute name="authors" value="Staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 11:50:29 AM"/>
        <attribute name="created" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMTk7MTE6MjM6NTUgQU07Mjg4Ng=="/>
        <attribute name="edited" value="U3RhZmY7REVTS1RPUC1IUEtPSzhSOzI1NjgtMDctMTk7MTE6NTA6MjkgQU07MTsyOTk1"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Interest, years, Totalyears" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <declare name="afterInterest, money, money1, money2, money3" type="Real" array="False" size=""/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="Totalyears"/>
            <while expression="years &lt;= Totalyears">
                <assign variable="money" expression="money + (money * (interest/100))"/>
                <output expression="&quot;Year&quot; &amp; years &amp; &quot;:&quot; &amp; money" newline="True"/>
                <assign variable="years" expression="years + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>